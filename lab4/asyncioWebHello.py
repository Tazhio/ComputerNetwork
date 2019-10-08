import asyncio


keys = ('method', 'path')

err404 = [b'HTTP/1.0 404 Not Found\r\n',
    b'Connection: close'
    b'Content-Type:text/html; charset=utf-8\r\n',
    b'\r\n',
b'<html><body>404 Not Found<body></html>\r\n', b'\r\n']
err504 = [b'HTTP/1.0 404 Not Found\r\n',
    b'Connection: close'
    b'Content-Type:text/html; charset=utf-8\r\n',
    b'\r\n',
b'<html><body>504 Method Not Allowed<body></html>\r\n', b'\r\n']

class HTTPHeader:
    def __init__(self):
        self.headers = {key: None for key in keys}

    def parse_header(self, line):
        fileds = line.split(' ')
        if fileds[0] == 'GET' or fileds[0] == 'HEAD':
            #to check whether the method is allowed or not
            self.headers['method'] = fileds[0]
            self.headers['path'] = fileds[1]
        else:return 504

    def get(self, key):
        return self.headers.get(key)


async def dispatch(reader, writer):
    while True:
        data = await reader.readline()
        message = data.decode().split(' ')
        print(data)
        if data == b'\r\n':
            break
    writer.writelines([
        b'HTTP/1.0 200 OK\r\n',
        b'Content-Type:text/html; charset=utf-8\r\n',
        b'Connection: close\r\n',
        b'\r\n',
        b''' <html><head><title>Index of .//</title></head>
    <body bgcolor="white">
    <h1>Index of .//</h1><hr>
    <pre>
    <a href="dir1/">dir1/</a><br>
    <a href="dir2/">dir2/</a><br>
    <a href="file1">file1</a><br>
    <a href="file1">file1</a><br>
    </pre>
    <hr>
    </body></html>
\r\n''',
        b'\r\n'
    ])
    await writer.drain()
    writer.close()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(dispatch, '127.0.0.1', 8080, loop=loop)
    server = loop.run_until_complete(coro)
    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

