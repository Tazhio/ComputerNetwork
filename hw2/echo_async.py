import asyncore


class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data=self.recv(2048)#buffer size
        if data and data!=b'exit\r\n': #if it equals exit, we quit
            self.send(data)



class EchoServer(asyncore.dispatcher):
    def __init__(self,address,port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((address,port))
        self.listen(10)
    def handle_accepted(self,sock,addr):
        print('Now we are serving address{}'.format(repr(addr))) #showing the current address we're serving
        handler=EchoHandler(sock)


if __name__=='__main__':
    try:
        server=EchoServer('127.0.0.1',5555)
        asyncore.loop()
    except KeyboardInterrupt:
        exit()
