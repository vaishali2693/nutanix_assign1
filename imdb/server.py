
import threading
import socket
import logging

class _server():

    def __init__(self):
        logging.info('Initializing Broker')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1', 4242))
        self.clients_list = []

    def talkToClient(self, ip):
        logging.info("Sending 'ok' to %s", ip)
        self.sock.sendto("ok", ip)

    def listen_clients(self):
        while True:
            msg, client = self.sock.recvfrom(1024)
            logging.info('Received data from client %s: %s', client, msg)
            #t = threading.Thread(target=self.talkToClient, args=(client,))
            #t.start()
            self.talkToClient(client)
            print msg#


if __name__ == '__main__':
    # Make sure all log messages show up
    logging.getLogger().setLevel(logging.DEBUG)

    b = _server()
    b.listen_clients()

