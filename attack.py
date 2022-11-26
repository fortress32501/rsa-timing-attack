import rsa_helper_functions as rsa
import datetime
import math
import statistics
from time import sleep

def avg(list_avg):
    return sum(list_avg)/len(list_avg)

def modpow(b, e, n):
	# find length of e in bits
	tst = 1
	siz = 0
	while e >= tst:
		tst <<= 1
		siz += 1
	siz -= 1
	# calculate the result
	r = 1
	for i in range(siz, -1, -1):
		r = (r * r) % n
		if (e >> i) & 1: r = (r * b) % n
	return r

def find_next_msgs(exp):
    exp = exp*2
    for i in range(100000, 109264138416697818087405225408360205259):
        val = modpow(i, exp, 109264138416697818087405225408360205259)
        #val = 1
        #for j in range(exp):
        #    val = val * i
        #    val = val % 109264138416697818087405225408360205259
        #val = i**exp % 109264138416697818087405225408360205259
        val = val * i
        if (val < 109264138416697818087405225408360205259):
            val2 = (i+1)**exp % 109264138416697818087405225408360205259
            val2 = val2 * (i+1)
            if (val2 > 109264138416697818087405225408360205259):
                print(str(i) + "|" + str(i+1))
                return i, i+1


p = 10756597338015291223
q = 10157871953665436333
n = p*q
keys = rsa.keysgen(p,q)
priv = keys['priv']
pub = keys['pub']

e = 302551102930460433882826511866637858843
#d = 103850030957717363945220809541239332931

exp = 1
binary_d = '1'
less_than = [4780711634765, 40522424, 16836, 7242663, 5545145, 686069, 822434, 533735, 1352774, 110356, 461916, 158819, 131833, 154773, 529115, 407660, 2341990, 508552, 149415, 103434, 190683, 184723, 452393, 205670, 343223]
greater_than = [4780711634965, 40522444, 16856, 7242664, 5545146, 686070, 822435, 533736, 1352775, 110357, 461917, 158820, 131834, 154774, 529116, 407661, 2341991, 508553, 149416, 103435, 190684, 184724, 452394, 205671, 343224]
for i in range(len(less_than)+10):
    msg, msg2 = '',''
    if ( i < len(less_than) ):
        msg, msg2 = less_than[i], greater_than[i]
    else:
        msg, msg2 = find_next_msgs(exp)
    

    list_t1 = []
    list_t2 = []
    for j in range(1):
        dec, time1 = rsa.numdecrypt(msg, priv)
        dec2, time2 = rsa.numdecrypt(msg2, priv)
        list_t1.append(time1)
        list_t2.append(time2)

    avg_1 = avg(list_t1)
    avg_2 = avg(list_t2)
    if (avg_2 - avg_1 > 0):
        binary_d += '1'
        exp = exp*2+1
    else:
        binary_d += '0'
        exp = exp*2
    print(binary_d)
