import rsa_helper_functions as rsa
import datetime
# works except for large values of msg
start_time = datetime.datetime.now()

for i in range(10000):
    p = 218937333647866515174974508976298574113 #rsa.genprime(128)
    q = 305135019088425420963600975979560333313 #rsa.genprime(128)
    #print(p)
    #print(q)
    keys = rsa.keysgen(p,q)
    #print(keys)
    priv = keys['priv']
    pub = keys['pub']

    msg = 65155816516404964423665942839901505741918105972355201219561059350821498022767
    msg_bytes = msg.to_bytes(256, 'big')
    enc = rsa.encrypt_bytes(msg_bytes, pub)
    dec = rsa.decrypt_bytes(enc, priv)
    test=0

end_time = datetime.datetime.now()

print(test.from_bytes(dec,'big'))

time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000 / 10000

print(execution_time)