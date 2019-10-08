import socket
def echo():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ipv4, tcp
    sock.bind(('127.0.0.1',5555))
    sock.listen(10)
    #socket.listen(backlog) Listen for connections made to the socket.
    # The backlog argument specifies the maximum number of queued connections and should be at least 1;
    # the maximum value is system-dependent (usually 5).
    while True:
        conn,address=sock.accept()
        while True:
            data=conn.recv(2048)#buff size #recv: receive
            if data and data !=b'exit\r\n':
                conn.send(data)
                print(data)
            else:
                conn.close()
                break
#bug总算找到了，原来是break的缩进错了。

if __name__=='__main__':
    try:
        echo()
    except KeyboardInterrupt:
        exit()

