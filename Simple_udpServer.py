from socket import *
serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print ("UDP server\n")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message,"utf-8") #cp1252 #utf-8

    decryptedMessage = ""
    for i in range(len(text)):
        utf8Code = ord(text[i])
        decryptedChar = chr(utf8Code - 3)
        decryptedMessage += decryptedChar

    print ("Received from Client: ", decryptedMessage)