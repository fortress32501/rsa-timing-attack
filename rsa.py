import rsa_helper_functions as rsa
import datetime
import math
import statistics

def avg(list_avg):
    return sum(list_avg)/len(list_avg)

def std_dev(list_std):
    mean = sum(list_std) / len(list_std)
    variance = sum([((x - mean) ** 2) for x in list_std]) / (len(list_std)-1)
    return variance ** 0.5

def convert_to_one_list(list_t, list_c, d):
    list_sub1 = []
    list_sub2 = []
    for i in range(len(list_t)):
        list_sub1.append(list_t[i]-list_c[i]-d)
        list_sub2.append(list_t[i]-list_c[i])
    return list_sub1, list_sub2

def density(x, mean, std_dev):
    exp = -((x-mean)**2) / (2 * (std_dev**2))
    return (math.e ** (exp)) / (std_dev * ((math.pi * 2) ** 0.5))

def prob(t, c, d, mean_1, std_dev_1, mean_0, std_dev_0):
    x1 = ((t-c-d) - (mean_1)) / (std_dev_1)
    prob_of_1 = density(t-c-d, mean_1, std_dev_1)

    x0 = ((t-c) - (mean_0)) / (std_dev_0)
    prob_of_0 = density(t-c, mean_0, std_dev_0)

    print(prob_of_1)
    print(prob_of_0)
    return prob_of_1, prob_of_0

def total_prob(list_t, list_c, d):
    list1, list0 = convert_to_one_list(list_t, list_c, d)

    sum_top = 0
    sum_bottom = 0
    mean_1, std_dev_1, mean_0, std_dev_0 = avg(list1), std_dev(list1), avg(list0), std_dev(list0)
    for i in range(len(list_t)):
        prob_of_1, prob_of_0 = prob(list_t[i], list_c[i], d, mean_1, std_dev_1, mean_0, std_dev_0)
        #print(prob_of_1 / (prob_of_1 + prob_of_0))
        sum_top += prob_of_1
        sum_bottom += prob_of_1 + prob_of_0

    return sum_top / sum_bottom


p = 218937333647866515174974508976298574113 #rsa.genprime(128)
q = 305135019088425420963600975979560333313 #rsa.genprime(128)
#print(p)
#print(q)
keys = rsa.keysgen(p,q)
#print(keys)
priv = keys['priv']
pub = keys['pub']

# From 54,800,000 runs
d = 1.556249
list_t = []
list_c = []
time = 0

for i in range(100000):
    msg = 67055495 + i**7
    msg_bytes = msg.to_bytes(256, 'big')
    enc, temp = rsa.encrypt_bytes(msg_bytes, pub)
    
    dec, time = rsa.decrypt_bytes(enc, priv)
    
    # appends time t to list
    list_t.append(time)

    guess = '110011000100011111001111001001001000010110110'+'1'
    guess_num = int(guess, 2)
    dec1, time = rsa.decrypt_bytes_guess(enc, priv, guess_num, len(guess))
    
    # appends time c to list 
    list_c.append(time)

test=0
print(test.from_bytes(dec,'big'))
#prob = total_prob(list_t, list_c, d)
#print(prob)

#avg_t = avg(t)
#std_dev_t = std_dev(t)
#var_t = std_dev(t)**2
#print(avg_t) = 1.7939273482142857
#print(std_dev_t) = 6.6924724150218236
#print(var_t) = 44.78918702582804
#print(len(t)) = 112000000
var_t = 44.78918702582804

# # From 2,000,000 runs
# var_e = 0.00021535195762530283
# e_avg = 0.001502460500016142

avg_total_time = avg(list_t)
avg_guess_time = avg(list_c)
list_rest_time = []
for i in range(len(list_t)):
    list_rest_time.append(list_t[i] - list_c[i])

w = 256
b = 46
c = 45
var_rest = statistics.variance(tuple(list_rest_time))
var_expected_correct = (w - b)*(var_t)
var_expected_wrong = (w - b + 2*c)*(var_t)
print(var_rest)
print(var_expected_correct)
print(var_expected_wrong)

# print(avg(d)) = 1.556249
# print(std_dev(d)) = 1.3259245106882933
# print(std_dev(d)**2) = 1.75807580804399
# print(len(d)) = 1000000

#print(avg(t)) = 0.001926075425887225
#print(std_dev(t)) = 0.00726641937118175
#print(std_dev(t)**2)