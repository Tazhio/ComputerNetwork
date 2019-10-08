import socket


hello = [b'HTTP/1.0 200 OK\r\n',
b'Connection: close' b'Content-Type:text/html; charset=utf-8\r\n', b'\r\n',
    b'''<html><head><title>Index of .//</title></head>
    <body bgcolor="white">
    <h1>Index of .//</h1><hr>
    <pre>
    <a href="dir1/">dir1/</a><br>
    <a href="dir2/">dir2/</a><br>
    <a href="file1">file1</a><br>
    <a href="file1">file1</a><br>
    </pre>
    <hr>
    </body></html>   ''' ,
    b'\r\n']


err404 = [b'HTTP/1.0 404 Not Found\r\n',
    b'Connection: close'
    b'Content-Type:text/html; charset=utf-8\r\n',
    b'\r\n',
b'<html><body>404 Not Found<body></html>\r\n', b'\r\n']

def web():
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(10)
    while True:
        conn,address=sock.accept()
        data=conn.recv(2048).decode().split('\r\n')
        print(data[0].split(' '))
        res=err404
        if data[0].split(' ')[1]=='/':
            res=hello
        for line in res:
            conn.send(line)
        conn.close()

keys = ('method', 'path')

class HTTPHeader:
    def __init__(self):
        self.headers = {key: None for key in keys}

    def parse_header(self, line):
        fileds = line.split(' ')
        if fileds[0] == 'GET' or fileds[0] == 'HEAD':
            self.headers['method'] = fileds[0]
            self.headers['path'] = fileds[1]
        else:return 405


    def get(self, key):
        return self.headers.get(key)


if __name__=='__main__':
    try:
        web()
    except KeyboardInterrupt:
        exit()
