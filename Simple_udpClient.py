from socket import *
import random
import math
import time

def generate_random_4096_bits():
    num_bits = 2050
    num_bytes = (num_bits + 7) // 8  # Calculate the number of bytes required

    random_bytes = [random.randint(0, 255) for _ in range(num_bytes)]  # Generate random bytes
    random_number = int.from_bytes(random_bytes, byteorder='big')  # Convert bytes to an integer

    return random_number

def count_bits(number):
    if number == 0:
        return 1  # Special case for 0
    return int(math.log2(number)) + 1

def is_Prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Write n as (2^r) * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def GetBigPrimeNumber():
    
    num = generate_random_4096_bits()
    while is_Prime(num)==False:         
         num = generate_random_4096_bits()   
    return num

print("Gerando 'p'..")
start = time.time()
p=GetBigPrimeNumber()
end = time.time()
print("Demorou: "+str(end - start))
print("valor de p: "+str(p))

print("Gerando 'q'..")
start = time.time()
q=GetBigPrimeNumber()
end = time.time()
print("Demorou: "+str(end - start))
print("valor de q: "+str(q))


N=p*q
print("valor de 'N': " + str(N))

totiente = (p-1)*(q-1)
print("valor de 'totiente': " + str(totiente))


'''
serverName = "127.0.0.1" # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
print("UDP Client\n")
while 1:
    message = input("Input message: ")
    if message == "exit":
            break
    
    encryptedMessage = ""
    for i in range(len(message)):
        utf8Code = ord(message[i])
        encryptedChar = chr(utf8Code + 3)
        encryptedMessage += encryptedChar

    clientSocket.sendto(bytes(encryptedMessage,"utf-8"), (serverName, serverPort))
clientSocket.close()


'''
