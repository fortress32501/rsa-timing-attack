import rsa_helper_functions as rsa
import datetime

p = 122268303346395253640045626460453767786422963450545466762839293864594439747297186877559467374972718702332981464615953149969022070292856347465555122516910787542372106052021933886423524974390513988272527646854598922046299728924034036008007844822138074670732751285044783549328437289356678531826832462130865091513
q = 137449236222080828470535550143721995814732648560696658386854799600170201111725381715767576962662987213387795964330927097996369725918946473706925305134842154246066024662529174871258360671232942498718250070439253112164394107784433300563256874745255402795213615667111377357420049808527790552212498192946363134153
#print(p)
#print(q)
keys = rsa.keysgen(p,q)
#print(keys)
priv = keys['priv']
pub = keys['pub']

total_time = 0
for i in range(10000):
    if i%10000 == 0:
        print(i)
    msg = 1374492362220808284705355501437219958147326485606966583868547996001702011117253817157675769626629872133877959643309270979963697259189464737069253051348421542460660246625291748712583606712329424987182500704392531121643941077844333005632568747452554027952136156671 + i
    msg_bytes = msg.to_bytes(2048, 'big')
    enc = rsa.encrypt_bytes(msg_bytes, pub)
    
    start_time = datetime.datetime.now()
    dec = rsa.decrypt_bytes(enc, priv)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    total_time += time_diff.total_seconds()

test=0
print(test.from_bytes(dec,'big'))

execution_time = total_time * 1000 / 10000

print(execution_time)

total_time = 0
for i in range(10000): 
    if i%10000 == 0:
        print(i)
    msg = 137449236222080828470535550143721995814732648560696658386854799600170201111725381715767576962662987213387795964330927097996369725918946473706925305134842154246066024662529174871258360 + i
    msg_bytes = msg.to_bytes(256, 'big')
    enc = rsa.encrypt_bytes(msg_bytes, pub)
    
    start_time = datetime.datetime.now()
    dec = rsa.decrypt_bytes(enc, priv)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    total_time += time_diff.total_seconds()

test=0
print(test.from_bytes(dec,'big'))

execution_time = total_time * 1000 / 10000

print(execution_time)