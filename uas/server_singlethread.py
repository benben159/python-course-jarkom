import socket

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind(('127.0.0.1',9999))
sock_server.listen(1)
client, addr = sock_server.accept()
print 'koneksi client diterima: {}'.format(addr)
while True:
    try:
        balasan = client.recv(1024) ## 1024 adalah jumlah character yg diterima
        ## tulis logika pemrograman sesuai dengan yang diinginkan
        ## di dalam soal
        ## balasan = ...
        client.send(balasan)
        ##          ^^^^^^^
        ## set pesan yang akan dikirim ke 
        ## client dalam variabel ini
    except Exception as e:
        break
    except KeyboardInterrupt as k:
        break

