import rsa_helper_functions as rsa
import datetime
import math
import statistics
from time import sleep

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


#p = 218937333647866515174974508976298574113 #rsa.genprime(128)
#q = 305135019088425420963600975979560333313 #rsa.genprime(128)
#print(p)
#print(q)
p = 10756597338015291223
q = 10157871953665436333
e = 302551102930460433882826511866637858843
d = 103850030957717363945220809541239332931

# cube root of n = 40576130234080252707404486
# < cube root of n = 40576130234080252707400000
# > cube root of n = 40576130234080252707480000

# 2317193894253193
# 6369939578526
# 94400245847
keys = rsa.keysgen(p,q)
#print(keys)
priv = keys['priv']
pub = keys['pub']

# From 54,800,000 runs
d = 1.556249
list_t1 = []
list_t2 = []
time = 0
time2 = 0

#for i in range(686069, 109264138416697818087405225408360205259):
#    val = i**78 % 109264138416697818087405225408360205259
#    val = val * i
#    if (val > 109264138416697818087405225408360205259):
#        print(i)
#5545145
for i in range(1):
    #msg = 4780711634765
    #msg2 = 4780711634965 #to the 3
    #msg = 40522424
    #msg2 = 40522444 # to the 5
    #msg = 16836
    #msg2 = 16856 # to the 9
    #msg = 7242663
    #msg2 = 7242664 # 19
    #msg = 5545145
    #msg2 = 5545146 # to the 39
    msg = 686069
    msg2 = 686070 # to the 78

    dec, time1 = rsa.numdecrypt(msg, priv)
    dec2, time2 = rsa.numdecrypt(msg2, priv)
    list_t1.append(time1)
    list_t2.append(time2)

    #guess = '110011000100011111001111001001001000010110110'+'1'
    #guess_num = int(guess, 2)
    #dec1, time = rsa.decrypt_bytes_guess(enc, priv, guess_num, len(guess))

    
print(dec)

avg_1 = avg(list_t1)
avg_2 = avg(list_t2)
print(avg_1)
print(avg_2)
print(avg_2-avg_1)

#prob = total_prob(list_t, list_c, d)
#print(prob)

#avg_t = avg(t)
#std_dev_t = std_dev(t)
#var_t = std_dev(t)**2
#print(avg_t) = 1.7939273482142857
#print(std_dev_t) = 6.6924724150218236
#print(var_t) = 44.78918702582804
#print(len(t)) = 112000000
#var_t = 44.78918702582804

# # From 2,000,000 runs
# var_e = 0.00021535195762530283
# e_avg = 0.001502460500016142

# avg_total_time = avg(list_t)
# avg_guess_time = avg(list_c)
# list_rest_time = []
# for i in range(len(list_t)):
#     list_rest_time.append(list_t[i] - list_c[i])

# w = 256
# b = 46
# c = 45
# var_rest = statistics.variance(tuple(list_rest_time))
# var_expected_correct = (w - b)*(var_t)
# var_expected_wrong = (w - b + 2*c)*(var_t)
# print(var_rest)
# print(var_expected_correct)
# print(var_expected_wrong)

# print(avg(d)) = 1.556249
# print(std_dev(d)) = 1.3259245106882933
# print(std_dev(d)**2) = 1.75807580804399
# print(len(d)) = 1000000

#print(avg(t)) = 0.001926075425887225
#print(std_dev(t)) = 0.00726641937118175
#print(std_dev(t)**2)

#msg =  40576130234080252707400000 - i
    #msg2 = 40576130234080252707480000 - i to the 3
    #msg =  2317193894250000 - i
    #msg2 = 2317193894254193 - i
    #msg = 6369939578500
    #msg2 = 6369939578626 
    #msg = 94400245800
    #msg2 = 94400245947 to the 7
    #msg = 812080
    #msg2 = 812183 #to the 13
    #msg = 1180
    #msg2 = 1193 #to the 25
    #msg = 30
    #msg2 = 34 #to the 51