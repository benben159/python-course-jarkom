import socket
import threading

def handle_client(sock_client, addr):
    ##logging.debug('client connection accepted: {}'.format(addr))
    message = sock_client.recv(1024)
    ## tulis logika pemrograman sesuai dengan yang diinginkan
    ## di dalam soal
    sock_client.send(server_message)
    ##               ^^^^^^^^^^^^^^
    ##     set pesan yang akan dikirim ke 
    ##     client dalam variabel ini
    sock_client.close()

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind(('127.0.0.1',9999))
sock_server.listen(5)
clients = []
while True:
    try:
        s, a = sock_server.accept()
        t_client = threading.Thread(target=handle_client, args=(s,a))
        t_client.start()
        t_client.join(1)
        clients.append(t_client)
    except Exception as e:
        logging.debug(e)
        break
    except KeyboardInterrupt as k:
        break
