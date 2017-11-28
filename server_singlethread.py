import socket

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind(('127.0.0.1',9999))
sock_server.listen(1)
client, addr = sock_server.accept()
print 'koneksi client diterima: {}'.format(addr)
while True:
    try:
        #client.send('hello client')
        balasan = client.recv(1024) ## 1024 adalah jumlah character yg diterima
        balasan = 'anda menulis: {}'.format(balasan)
        client.send(balasan)
    except Exception as e:
        break
    except KeyboardInterrupt as k:
        break

