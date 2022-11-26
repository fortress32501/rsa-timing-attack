import rsa_helper_functions as rsa
import datetime

time=[]
for i in range(10000000):
    val = 13524353262345654643564363245353264325436243636346*(i+1)**2
    start_time = datetime.datetime.now()		
    val = val % 1352435326234565464356436324535
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    time_val = time_diff.total_seconds()
    time.append(time_val)

print(time[1000])
print(time[1000000])
print(sum(time)/len(time))
#p = rsa.genprime(64)
#q = rsa.genprime(64)
#print(p)
#print(q)
#keys = rsa.keysgen2(p,q)
#print(keys)
#priv = keys['priv']
#pub = keys['pub']

# total_time = 0
# for i in range(10000):
#     if i%10000 == 0:
#         print(i)
#     msg = 1374492362220808284705355501437219958147326485606966583868547996001702011117253817157675769626629872133877959643309270979963697259189464737069253051348421542460660246625291748712583606712329424987182500704392531121643941077844333005632568747452554027952136156671 + i
#     msg_bytes = msg.to_bytes(2048, 'big')
#     enc = rsa.encrypt_bytes(msg_bytes, pub)
    
#     start_time = datetime.datetime.now()
#     dec = rsa.decrypt_bytes(enc, priv)
#     end_time = datetime.datetime.now()
#     time_diff = (end_time - start_time)
#     total_time += time_diff.total_seconds()

# test=0
# print(test.from_bytes(dec,'big'))

# execution_time = total_time * 1000 / 10000

# print(execution_time)

# total_time = 0
# for i in range(10000): 
#     if i%10000 == 0:
#         print(i)
#     msg = 137449236222080828470535550143721995814732648560696658386854799600170201111725381715767576962662987213387795964330927097996369725918946473706925305134842154246066024662529174871258360 + i
#     msg_bytes = msg.to_bytes(256, 'big')
#     enc = rsa.encrypt_bytes(msg_bytes, pub)
    
#     start_time = datetime.datetime.now()
#     dec = rsa.decrypt_bytes(enc, priv)
#     end_time = datetime.datetime.now()
#     time_diff = (end_time - start_time)
#     total_time += time_diff.total_seconds()

# test=0
# print(test.from_bytes(dec,'big'))

# execution_time = total_time * 1000 / 10000

# print(execution_time)