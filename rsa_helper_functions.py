import secrets
import datetime
from time import sleep

def eucalg(a, b):
	# make a the bigger one and b the lesser one
	swapped = False
	if a < b:
		a, b = b, a
		swapped = True
	# ca and cb store current a and b in form of
	# coefficients with initial a and b
	# a' = ca[0] * a + ca[1] * b
	# b' = cb[0] * a + cb[1] * b
	ca = (1, 0)
	cb = (0, 1)
	while b != 0:
		# k denotes how many times number b
		# can be substracted from a
		k = a // b
		# a  <- b
		# b  <- a - b * k
		# ca <- cb
		# cb <- (ca[0] - k * cb[0], ca[1] - k * cb[1])
		a, b, ca, cb = b, a-b*k, cb, (ca[0]-k*cb[0], ca[1]-k*cb[1])
	if swapped:
		return (ca[1], ca[0])
	else:
		return ca

def modpow_guess(b, e, n, size):
	r = 1
	for i in range(size, -1, -1):
		r = (r * r) % n
		if (e >> i) & 1:
			r = (r * b) % n
	return r

def mod(x, n):
	if (x >= n):
		x = x % n
	return x

def modpow(b, e, n):
	r = b
	time = 0
	for i in range(125, -1,-1):
		if (r*r > n):
			time += 0.000005
		r = mod(r * r, n)
		time += 0.00001
		if (e >> i) & 1:
			if (r*b > n):
				time += 0.000005
			r = mod(r * b, n)
			time += 0.00001
	# r = 1
	# for i in range(256):
	# 	if (e >> i) & 1:
	# 		r = mod(r * b, n)
	# 	b = mod(b * b, n)
	return r, time

def keysgen(p, q):
	n = p * q
	lambda_n = (p - 1) * (q - 1)
	
	#e = 65155816516404964423665942839901505741918105972355201219561059350821498022767 #genprime(256)
	#d = 92398696898745912779430978791596083401900812537362926530750597110273663259535 #eucalg(e, lambda_n)[0]
	#d = 63450674589416863923538232539424106438583316370952785520886201108295380849551
	#d = 106872708053410437207377351917682071883559560620567997035682795111262804464527
	#d = 99635702476078174993404165354639077642730186578965461783216696110768233862031
	#d = 88780194110079781672444385510074586281486125516561658904517547610026377958287
	#d = 90589445504412847225937682150835334841693469026962292717634072360150020608911

	e = 302551102930460433882826511866637858843
	#d = 103850030957717363945220809541239332931
	#d = 146385326822834671878142635470210359363
	#d = 125117678890276017911681722505724846147
	#d = 93216206991438036961990353058996576323
	#d = 98533118974577700453605581300117954627
	#d = 101191574966147532199413195420678643779
	#d = 105179258953502279818124616601519677507
	if d < 0: d += lambda_n
        # both private and public key must have n stored with them
	return {'priv': (d, n), 'pub': (e, n)}

def numencrypt(m, pub):
	#start_time = datetime.datetime.now()		
	c, time = modpow(m, pub[0], pub[1])
	#end_time = datetime.datetime.now()
	#time_diff = (end_time - start_time)
	#time_val = time_diff.total_seconds() * 1000000
	#time = time_val
	return c, time*1000000

def numdecrypt(m, priv):
	#start_time = datetime.datetime.now()		
	c, time = modpow(m, priv[0], priv[1])
	#end_time = datetime.datetime.now()
	#time_diff = (end_time - start_time)
	#time_val = time_diff.total_seconds() * 1000000
	#time = time_val
	return c, time*1000000

########### For better RSA ###########
# matrix multiplication
def sqmatrixmul(m1, m2, w, mod):
	mr = [[0 for j in range(w)] for i in range(w)]
	for i in range(w):
		for j in range(w):
			for k in range(w):
				mr[i][j] =(mr[i][j]+m1[i][k]*m2[k][j])%mod
	return mr

# fibonacci calculator
def fib(x, mod):
	if x < 3: return 1
	x -= 2
	# find length of e in bits
	tst = 1
	siz = 0
	while x >= tst:
		tst <<= 1
		siz += 1
	siz -= 1
	# calculate the matrix
	fm = [
		# function matrix
		[0, 1],
		[1, 1]
	]
	rm = [
		# result matrix
		# (identity)
		[1, 0],
		[0, 1]
	]
	for i in range(siz, -1, -1):
		rm = sqmatrixmul(rm, rm, 2, mod)
		if (x >> i) & 1:
			rm = sqmatrixmul(rm, fm, 2, mod)

	# second row of resulting vector is result
	return (rm[1][0] + rm[1][1]) % mod

def genprime(siz):
	while True:
		num = (1 << (siz - 1)) + secrets.randbits(siz - 1) - 10;
		# num must be 3 or 7 (mod 10)
		num -= num % 10
		num += 3 # 3 (mod 10)
		# heuristic test
		if modpow(2, num - 1, num) ==1 and fib(num + 1, num) ==0:
			return num
		num += 5 # 7 (mod 10)
		# heuristic test
		if modpow(2, num - 1, num) ==1 and fib(num + 1, num) ==0:
			return num

def encrypt_bytes(data, key):
	data = bytearray(data)
	cdata = bytearray()
	time = 0
	for i in range(0, len(data), 256):
		# read 256 bytes and store as long
		# to m
		m = 0
		for j in range(256):
			if i + j < len(data):
				m = (m << 8) + data[i + j]
			else:
				m <<= 8
		# encrypt m
		start_time = datetime.datetime.now()		
		c = modpow(m, key[0], key[1])
		end_time = datetime.datetime.now()
		time_diff = (end_time - start_time)
		time_val = time_diff.total_seconds() * 1000000
		time = time_val
		# store c into cdata
		for j in range(255, -1, -1):
			cdata.append((c >> (j * 8)) & 255)
	return bytes(cdata), time

# both functions are essencially the same,
# the only difference is in which key you use
decrypt_bytes = encrypt_bytes

def encrypt_bytes_guess(data, key, guess, size):
	data = bytearray(data)
	cdata = bytearray()
	time = 0.0
	for i in range(0, len(data), 256):
		# read 256 bytes and store as long
		# to m
		m = 0
		for j in range(256):
			if i + j < len(data):
				m = (m << 8) + data[i + j]
			else:
				m <<= 8
		# encrypt m
		start_time = datetime.datetime.now()		
		c = modpow_guess(m, guess, key[1], size)
		end_time = datetime.datetime.now()
		time_diff = (end_time - start_time)
		time_val = time_diff.total_seconds() * 1000000
		time = time_val
		# store c into cdata
		for j in range(255, -1, -1):
			cdata.append((c >> (j * 8)) & 255)
	return bytes(cdata), time

# both functions are essencially the same,
# the only difference is in which key you use
decrypt_bytes_guess = encrypt_bytes_guess
