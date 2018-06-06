import socket
SIZE = 1024	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
s.connect(('10.211.55.3', 8080))				
print s.recv(SIZE)
s.send('begin to send')							
print 'sending, please wait for a second ...'
with open('./Head First Python.pdf', 'rb') as f:			
    for data in f:
        s.send(data)
print 'sended !'
s.close()
print 'connection closed'