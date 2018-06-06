import socket, threading, os

SIZE = 1024

def checkFile():
    list = os.listdir('.')
    for iterm in list:
        if iterm == 'Head First Python.pdf':
            os.remove(iterm)
            print 'remove'
        else:
            pass

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome from server!')
    print 'receiving, please wait for a second ...'
    while True:
        data = sock.recv(SIZE)
        if not data :
            print 'reach the end of file'
            break
        elif data == 'begin to send':
            print 'create file'
            checkFile()
            with open('./Head First Python.pdf', 'wb') as f:
                pass
        else:
            with open('./Head First Python.pdf', 'ab') as f:
                f.write(data)
    sock.close()
    print 'receive finished'
    print 'Connection from %s:%s closed.' % addr


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.211.55.3',8080))
s.listen(1)
print 'Waiting for connection...'
while True:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()
