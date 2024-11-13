import hashlib,sys

def FindNonce(strToHash:str,intBitsZero:int):
    BitsZero = b'0'*intBitsZero
    Contador = 0
    strToByte = strToHash.encode(encoding='UTF-8', errors='strict')
    while Contador <= 2**32:
        
        Hexs = [hashlib.sha256((Contador+i).to_bytes(4,'big') + strToByte).digest() for i in range(2**15)]
        print(Hexs[0] == BitsZero)
            # Pegando os Bytes para comparação
        for i in range(0,len(Hexs),11):
            Byte1,Byte2,Byte3,Byte4 = bin(Hexs[i][0]),bin(Hexs[i][1]),bin(Hexs[i][2]),bin(Hexs[i][3])
            Nonce = Byte1[2:] + Byte2[2:] + Byte3[2:] + Byte4[2:]
            Nonce1 = Nonce[0:intBitsZero]

            Byte1,Byte2,Byte3,Byte4 = bin(Hexs[i+1][0]),bin(Hexs[i+1][1]),bin(Hexs[i+1][2]),bin(Hexs[i+1][3])
            Nonce = Byte1[2:] + Byte2[2:] + Byte3[2:] + Byte4[2:]
            Nonce2 = Nonce[0:intBitsZero]

            Byte1,Byte2,Byte3,Byte4 = bin(Hexs[i+2][0]),bin(Hexs[i+2][1]),bin(Hexs[i+2][2]),bin(Hexs[i+2][3])
            Nonce = Byte1[2:] + Byte2[2:] + Byte3[2:] + Byte4[2:]
            Nonce3 = Nonce[0:intBitsZero]

            Byte1,Byte2,Byte3,Byte4 = bin(Hexs[i+3][0]),bin(Hexs[i+3][1]),bin(Hexs[i+3][2]),bin(Hexs[i+3][3])
            Nonce = Byte1[2:] + Byte2[2:] + Byte3[2:] + Byte4[2:]
            Nonce4 = Nonce[0:intBitsZero]
            if Nonce1 == BitsZero or Nonce2 == BitsZero or Nonce3 == BitsZero or Nonce4 == BitsZero:
                break
            
        Contador += 2**15
        '''4294967296'''
        print(Contador)

        
        
        # Comparando para ver se é o Nonce certo
        


    return 'Olá',10