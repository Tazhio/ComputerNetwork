import socket, threading


class Echo(threading.Thread):
    def __init__(self, conn, address):
        threading.Thread.__init__(self)
        self.conn = conn
        self.address = address


def run(self):
    while True:
        data = self.conn.recv(2048)
        if data and data != b'exit\r\n':
            self.conn.send(data)
            print('{} sent: {}'.format(self.address, data))
        else:
            self.conn.close()
            return


def echo():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #选择 AF_INET 的目的就是使用 IPv4 进行通信。因为 IPv4 使用 32 位地址，相比 IPv6 的 128 位来说，计算更快，便于用于局域网通信。
    #新套接口的类型描述类型，如TCP（SOCK_STREAM）和UDP（SOCK_DGRAM）。
    #SOCK_STREAM 提供有序的、可靠的、双向的和基于连接的字节流，使用带外数据传送机制，为Internet地址族使用TCP。
    #SOCK_DGRAM 支持无连接的、不可靠的和使用固定大小（通常很小）缓冲区的数据报服务，为Internet地址族使用UDP。
    sock.bind(('127.0.0.1', 5555))
    sock.listen(10)
    while True:
        #在python中是可以使用连续赋值的方式来一次为多个变量进行赋值的
        conn, address = sock.accept()
        Echo(conn, address).start()


if __name__ == "__main__":
    try:
        echo()
    except KeyboardInterrupt:
        exit()