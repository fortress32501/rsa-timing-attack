import rsa_helper_functions as rsa
import datetime

p = 218937333647866515174974508976298574113 #rsa.genprime(128)
q = 305135019088425420963600975979560333313 #rsa.genprime(128)
#print(p)
#print(q)
keys = rsa.keysgen(p,q)
#print(keys)
priv = keys['priv']
pub = keys['pub']


total_time = 0
for i in range(400000):
    msg = 67055495320173175376786367218002717475 + i
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