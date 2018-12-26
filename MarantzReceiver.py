import Receiver
import logging
import time
import select
import socket

logger = logging.getLogger(__name__)

class marantz_receiver(Receiver.receiver):

    TCP_PORT = 23
    BUFFER_SIZE = 1024
    LINE_TERMINATOR = '\r'
    TIMEOUT = 1
    WAIT_AFTER_SEND = 1

    def __init__(self, hostname):
        print("connecting...")
        self.hostname = hostname
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((hostname, self.TCP_PORT))

#        intro = self.receive()
#        print(intro)

    def send(self, cmd):
        cmd = cmd.rstrip(self.LINE_TERMINATOR) + self.LINE_TERMINATOR
        send_data = bytes(cmd, 'ascii')
        logger.debug('sending: {}'.format(repr(send_data)))
        self.conn.send(send_data)
        time.sleep(self.WAIT_AFTER_SEND)

    def receive(self, timeout=TIMEOUT):
        ready = select.select([self.conn], [], [], timeout)
        if not ready[0]:
            raise Exception('Not ready to read data in the specified timeout time {} s'.format(timeout))
        data = self.conn.recv(self.BUFFER_SIZE)
        logger.debug('received: {}'.format(repr(data)))
        data = data.decode('ascii').strip(self.LINE_TERMINATOR)
        print("parsed " + data)
        return [line.strip() for line in data.split(self.LINE_TERMINATOR)]

    def change_source(self, source):
        print("changing source to " + source)
        self.send("SI" + source)

    def get_power(self):
        self.send('PW?')
        powerstatus = self.receive()
        print(powerstatus)
        if "PWON" in powerstatus[0]:
            return 1
        if "PWOFF" in powerstatus[0]:
            return 0

        raise Exception("I don't understand the response")

    def get_source(self):
        self.send("SI?")
        source = self.receive()
        return source[0]

    def disconnect(self):
        self.conn.close()