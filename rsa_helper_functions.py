import secrets
import datetime

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
	# calculate the result
	r = 1
	for i in range(size, -1, -1):
		r = (r * r) % n
		if (e >> i) & 1: r = (r * b) % n
	return r

def modpow(b, e, n):
	siz = 256
	# calculate the result
	r = 1
	for i in range(siz, -1, -1):
		r = (r * r) % n
		if (e >> i) & 1: 
			r = (r * b) % n
	return r

def keysgen(p, q):
	n = p * q
	lambda_n = (p - 1) * (q - 1)
	#e = 30062724333461455537324712521906829309940501958825960246810986932540692243696516740356271756228281685992532280566204960324911031407215394865063684351106244763099705921082663604847457831809211379434495169738068981733980601746777878604880067163922211371729441421728627444972863263386822410276556901397222629183225744179444653685937942388949190762869359231268326366272202792910164253974553873498222840640759035354917235644394918194856196465748071854991898670209588314982430921009186607852011456368580255308992538475873459323601588214130405300653321849814703830443858279481015855344558769243265313244114766248147670631313
	#d = 13722310453474723900411356356389689168809336501678726649372614457774484557622102515325156623473657896663001378493450158852264086417193271146059116727355329110558641441456773391127730932969466660898240143829605775791651371235348840156976651353715515720566889961575204992969328947086487423408498137373391002383360010799023534078549999260745594331576650855190288833082369244524256968234226516989541910710192529774081480078395588331849701776233299623513743147611094014796663444467171857267818228709259534743854050400589700162900552807615841115100299030643720889969066796427797509793364044149006771285998000417290521188977
	
	#e = 16866826212877955350329054683315463617109689359705070196464453980221614591114234955810621025786743343658823105147483141376325528987766151859993765670433571537364047290057829564074892825019782310137815315271941528347050210691320579232413441899038339982480771561983927241561779258875604149296128371709290813107879767553620996462638560959280797383984000345532039785041096016159537451619106695277596204258490143955966729398528823715174418087862456428237384364809383961773488046998155044378633259129338556618509665350882271453130911912734033225209519886488597410213001852945131631971581022090958373106754489445154468275613
	#d = 7647795216115734570719829419023872659907190755807298683971215595309842445432748306084215772677748049330627099248954968353024318916221362306062258707789145755343233795139055524768771493186435338830295418568549797764966527572476266672789112130153672279399974528052155417813885887672991467418111098563278582602768570431798169988378690320630833767988132597010848887160489642782380870226407130852070707508725806074178231335489608047636614345938814168465253413228585182729050500604954344252081058763389094590684324352676473970555079715504449512235252958904674793883984919633394644189159558993114344065122680394952329391989
	
	#e = 67055495320173175376786367218002717475005982339394790180005117886021808974703 #genprime(256)
	#d = 32398696898574912779430978791596083401900812537362926530750597110273663259535 #eucalg(e, lambda_n)[0]
	e = 65155816516404964423665942839901505741918105972355201219561059350821498022767 #genprime(256)
	d = 92398696898745912779430978791596083401900812537362926530750597110273663259535 #eucalg(e, lambda_n)[0]
	if d < 0: d += lambda_n
        # both private and public key must have n stored with them
	return {'priv': (d, n), 'pub': (e, n)}

def numencrypt(m, pub):
	return modpow(m, pub[0], pub[1])

def numdecrypt(m, priv):
	return modpow(m, priv[0], priv[1])

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
		c = modpow(m, key[0], key[1])
		# store c into cdata
		for j in range(255, -1, -1):
			cdata.append((c >> (j * 8)) & 255)
	return bytes(cdata)

# both functions are essencially the same,
# the only difference is in which key you use
decrypt_bytes = encrypt_bytes

def encrypt_bytes_guess(data, key, guess, size):
	data = bytearray(data)
	cdata = bytearray()
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
		c = modpow_guess(m, guess, key[1], size)
		# store c into cdata
		for j in range(255, -1, -1):
			cdata.append((c >> (j * 8)) & 255)
	return bytes(cdata)

# both functions are essencially the same,
# the only difference is in which key you use
decrypt_bytes_guess = encrypt_bytes_guess
