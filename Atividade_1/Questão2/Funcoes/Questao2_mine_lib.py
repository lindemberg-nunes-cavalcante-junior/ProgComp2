import hashlib,sys

def FindNonce(strToHash:str,intBitsZero:int):
    BitsZero = 0
    BitsZero = [BitsZero.to_bytes(1,'big') for _ in range(intBitsZero)]
    strToByte = strToHash.encode(encoding='UTF-8', errors='strict')
        
    Hexs = [hashlib.sha256((Contador+i).to_bytes(4,'big') + strToByte).digest() for i in range(2**32)]
        
    while True:
        # Pegando os Bytes para comparação
        for i in range(0,len(Hexs)):
            Byte1,Byte2,Byte3,Byte4 = bin(Hexs[i][0]),bin(Hexs[i][1]),bin(Hexs[i][2]),bin(Hexs[i][3])
            Nonce = Byte1[2:] + Byte2[2:] + Byte3[2:] + Byte4[2:]
            Nonce1 = Nonce[0:intBitsZero]
        # Comparando para ver se é o Nonce certo
            
        
    

        
        


    return 'Olá',10