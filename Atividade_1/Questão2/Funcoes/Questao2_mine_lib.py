import hashlib

def FindNonce(strToHash:str,intBitsZero:int):
    BitsZero = 0
    for i in range(2**32):
        a = i.to_bytes(4,'big')
        x = a + strToHash.encode(encoding='UTF-8', errors='strict')
        hex = hashlib.sha256(x).digest()
        teste = bin(hex[1])
        teste2 = hex[1]
        teste3 = teste[2:]
        print(teste,teste2,teste3)

    return 'Olá',10