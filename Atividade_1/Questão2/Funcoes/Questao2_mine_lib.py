import hashlib

def FindNonce(strToHash:str,intBitsZero:int):
    for i in range(2**32):
        a = i.to_bytes(4,'big')
        x = a + strToHash.encode()
        HEX = hashlib.sha256(x).digest()
        print(HEX)
    return 'Olá',10