import socket
import logging

logging.basicConfig(filename='example.log', format='[%(asctime)s] [%(level'
                                                   'name)s] => %(message)s',
                    level=logging.INFO)
logging.info('This message should go to the log file')

# Main event loop
def server(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print(f'Server up, running, and waiting for call on {host} {port}')
    logging.info(f'Server up, running, and waiting for call on {host} {port}')

    try:
        while True:
            conn, addr = sock.accept()
            process_request(conn, addr)

    finally:
        sock.close()

def process_request(conn, addr):
    file = conn.makefile()

    print(f'Received connection from {addr}')
    logging.info(f'Received connection from {addr}')

    try:
        while True:
            line = file.readline()
            if line:
                line = line.rstrip()
                print(f'{addr} --> {line}')
                logging.info(f'{addr} --> {line}')
                line_list = line.split(" ")
                if len(line_list) == 4:
                    number = line_list[0]
                    id_canal = line_list[1]
                    time = line_list[2]
                    group = line_list[3]
                    msg = f'спортсмен, нагрудный номер {number} прошёл ' \
                          f'отсечку {id_canal} в «{time[0:-2]}»\r\n'
                    logging.info(msg)
                    if group[0:2] == '00':
                        conn.sendall(msg.encode())
                else:
                    conn.sendall(b'unknown kind of data\r\n')
                if line == 'quit':
                    conn.sendall(b'connection closed\r\n')
                    logging.info('connection closed')
                    return

    finally:
        print(f'{addr} quit')
        logging.info(f'{addr} quit')
        file.close()
        conn.close()

if __name__ == '__main__':
    server('localhost', 5050)