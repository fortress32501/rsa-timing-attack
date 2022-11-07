import rsa_helper_functions as rsa
import datetime
import math

def total_prob(list_t, list_c, d):
    list1, list0 = convert_to_one_list(list_t, list_c, d)

    sum_top = 0
    sum_bottom = 0
    for i in range(len(list_t)):
        top, bottom = prob(list_t[i], list_c[i], d, avg(list1), std_dev(list1), avg(list0), std_dev(list0))
        sum_top += top
        sum_bottom += bottom

    return sum_top / sum_bottom

def prob(t, c, d, mean_1, std_dev_1, mean_0, std_dev_0):
    list1_mean = mean_1
    list1_std_dev = std_dev_1
    list0_mean = mean_0
    list0_std_dev = std_dve_0

    x1 = ((t-c-d) - (list1_mean)) / (list1_std_dev)
    prob_of_1 = density(x1)

    x0 = ((t-c) - (list0_mean)) / (list0_std_dev)
    prob_of_0 = density(x0)

    return prob_of_1, prob_of_1+prob_of_0

def density(x):
    return (math.e ** (-0.5*x*x)) / ((math.pi * 2) ** 0.5)

def covert_to_one_list(list_t, list_c, d):
    list_sub1[]
    list_sub2[]
    for i in range(len(list_t)):
        list_sub1.append(list_t[i]-list_c[i]-d)
        list_sub1.append(list_t[i]-list_c[i])

    return list_sub1, list_sub2

def std_dev(list_std):
    mean = sum(list_std) / len(list_std)
    variance = sum([((x - mean) ** 2) for x in list_std]) / len(list_std)
    return variance ** 0.5

def avg(list):
    return sum(list)/len(list)


p = 218937333647866515174974508976298574113 #rsa.genprime(128)
q = 305135019088425420963600975979560333313 #rsa.genprime(128)
#print(p)
#print(q)
keys = rsa.keysgen(p,q)
#print(keys)
priv = keys['priv']
pub = keys['pub']

# d = 0.002
# per loop: t = total_time, c = guess_time, d = 0.002
# mu(t-c-d) and std(t-c-d)
# AND mu(t-c) and std(t-c)

# Then P(1) = P(1)/Sum(P(0)andP(1))

total_time = 0
total_time1 = 0
for i in range(400000):
    msg = 67055495320173175376786367218002717475 + i
    msg_bytes = msg.to_bytes(256, 'big')
    enc = rsa.encrypt_bytes(msg_bytes, pub)
    
    start_time = datetime.datetime.now()
    dec = rsa.decrypt_bytes(enc, priv)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    total_time += time_diff.total_seconds()

    guess = '1'
    guess_num = int(guess, 2)
    start_time1 = datetime.datetime.now()
    dec1 = rsa.decrypt_bytes_guess(enc, priv, guess_num, 1)
    end_time1 = datetime.datetime.now()
    time_diff1 = (end_time1 - start_time1)
    total_time1 += time_diff1.total_seconds()

test=0
print(test.from_bytes(dec,'big'))


execution_time = total_time * 1000 / 400000
print(execution_time)

execution_time1 = total_time1 * 1000 / 400000
print(execution_time1)

total_time = 0
for i in range(400000): 
    msg = 6705549532017317 + i
    msg_bytes = msg.to_bytes(256, 'big')
    enc = rsa.encrypt_bytes(msg_bytes, pub)
    
    start_time = datetime.datetime.now()
    dec = rsa.decrypt_bytes(enc, priv)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    total_time += time_diff.total_seconds()

test=0
print(test.from_bytes(dec,'big'))

execution_time = total_time * 1000 / 400000
print(execution_time)