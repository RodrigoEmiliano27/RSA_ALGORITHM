
from socket import *
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


