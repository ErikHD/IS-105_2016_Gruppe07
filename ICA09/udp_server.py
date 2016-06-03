# Kode er hentet fra:
# http://www.binarytides.com/programming-udp-sockets-in-python
# Koden er tilvirket noe i forhold til ICA

import socket
import sys
 
HOST = ''   # Interface
PORT = 8888 # Tilgjengelig port
 
# UDP socket samt forbereder evt feilmelding
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
#  - sette opp forbindelsen
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#samhandler med klienten
while 1:
    # motta data fra klient (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
    if data == "Rev" :

        reply = 'Gratulerer, du hadde riktig svar: ' + data
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    else:

        reply = 'Feil svar, proev igjen!'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

     
s.close()