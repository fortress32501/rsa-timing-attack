import rsa_helper_functions as rsa
import datetime
import math

def avg(list_avg):
    return sum(list_avg)/len(list_avg)

# code edited from GEEKSFORGEEKS std_dev page
def std_dev(list_std):
    mean = sum(list_std) / len(list_std)
    variance = sum([((x - mean) ** 2) for x in list_std]) / len(list_std)
    return variance ** 0.5

def convert_to_one_list(list_t, list_c, d):
    list_sub1 = []
    list_sub2 = []
    for i in range(len(list_t)):
        list_sub1.append(list_t[i]-list_c[i]-d)
        list_sub2.append(list_t[i]-list_c[i])

    return list_sub1, list_sub2

def density(x):
    return (math.e ** (-0.5*x*x)) / ((math.pi * 2) ** 0.5)

def prob(t, c, d, mean_1, std_dev_1, mean_0, std_dev_0):
    x1 = ((t-c-d) - (mean_1)) / (std_dev_1)
    prob_of_1 = density(x1)

    x0 = ((t-c) - (mean_0)) / (std_dev_0)
    prob_of_0 = density(x0)

    return prob_of_1, prob_of_1+prob_of_0

def total_prob(list_t, list_c, d):
    list1, list0 = convert_to_one_list(list_t, list_c, d)

    sum_top = 0
    sum_bottom = 0
    for i in range(len(list_t)):
        if i%10000 == 0:
            print(i)
        top, bottom = prob(list_t[i], list_c[i], d, avg(list1), std_dev(list1), avg(list0), std_dev(list0))
        sum_top += top
        sum_bottom += bottom

    return sum_top / sum_bottom


p = 218937333647866515174974508976298574113 #rsa.genprime(128)
q = 305135019088425420963600975979560333313 #rsa.genprime(128)
#print(p)
#print(q)
keys = rsa.keysgen(p,q)
#print(keys)
priv = keys['priv']
pub = keys['pub']

d = 0.002
list_t = []
list_c = []

total_time = 0
total_time1 = 0
for i in range(10000):
    msg = 67055495 + i**10
    msg_bytes = msg.to_bytes(256, 'big')
    enc = rsa.encrypt_bytes(msg_bytes, pub)
    
    start_time = datetime.datetime.now()
    dec = rsa.decrypt_bytes(enc, priv)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    
    # appends time t to list
    list_t.append(time_diff.total_seconds() * 1000)

    guess = '1'
    guess_num = int(guess, 2)
    start_time1 = datetime.datetime.now()
    dec1 = rsa.decrypt_bytes_guess(enc, priv, guess_num, 1)
    end_time1 = datetime.datetime.now()
    time_diff1 = (end_time1 - start_time1)

    # appends time c to list 
    list_c.append(time_diff1.total_seconds() * 1000)

test=0
print(test.from_bytes(dec,'big'))

prob = total_prob(list_t, list_c, d)
print(prob)

# execution_time = total_time * 1000 / 400000
# print(execution_time)

# execution_time1 = total_time1 * 1000 / 400000
# print(execution_time1)

# total_time = 0
# for i in range(400000): 
#     msg = 6705549532017317 + i
#     msg_bytes = msg.to_bytes(256, 'big')
#     enc = rsa.encrypt_bytes(msg_bytes, pub)
    
#     start_time = datetime.datetime.now()
#     dec = rsa.decrypt_bytes(enc, priv)
#     end_time = datetime.datetime.now()
#     time_diff = (end_time - start_time)
#     total_time += time_diff.total_seconds()

# test=0
# print(test.from_bytes(dec,'big'))

# execution_time = total_time * 1000 / 400000
# print(execution_time)