# Author: Ayushi Patel
# I worked alone

import socket
import random
import time

localhost = "localhost"
listenPort = 3310
blazerID = "ayushi27"

# Initial connection to robot
print "Beginning connection.."
print ""
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket 1
s1.connect((localhost, listenPort)) # connecting
print "Connected."
print ""
s1.send(blazerID) # sending blazerID
print "Sent blazerID to robot.."
print ""
tcpPort = int(s1.recv(5))
print "Recieved the TCP port " + str(tcpPort) + " from robot.."
print ""
s1.close() # closing connection

print  "Listening for new connection.."
print ""
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket 2
s2.bind(('0.0.0.0', tcpPort)) # binding to tcpPort for incoming connection
s2.listen(5) # listening for incoming connection
connectionSocket, address = s2.accept() # accepting connection
print "Accepted new connection.."
print ""
udpPorts = connectionSocket.recv(12) # recieving message from robot
print "Received the UDP ports " + udpPorts + " from robot.."
print ""
s2.close()

s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creating socket 3
num = random.randint(6,9)
udpPort1 = int(udpPorts[0:5])
print "Sending " + str(num) + " to UDP port " + str(udpPort1)
s3.sendto(str(num), (localhost, udpPort1))
udpPort2 = int(udpPorts[6:11])

s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s4.bind(('0.0.0.0', udpPort2))
rand_num, address = s4.recvfrom(10 *int(num))
print ""
print "Recieved " + str(rand_num) + " on port " + str(udpPort2)
print ""
s4.close()

# s5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print "Sending UDP packets:"
for x in range(1,6):
    print "UDP packet " + str(x) + " sent"
    s3.sendto(str(rand_num), address)
    time.sleep(1)

print ""
print "Sent!"
