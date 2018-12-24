import Receiver
import telnetlib


class marantz_receiver(Receiver.receiver):

    def __init__(self, ip):
        print("connecting...")
        self.conn = telnetlib.Telnet(ip)
        intro = self.conn.read_eager()
        print(intro)
        pow = self.get_power()

    def change_source(self, source):
        print("changing source to " + source)

    def get_power(self):
        self.conn.write("PW?\r".encode("ascii"))
        powerstatus = self.conn.read_all()
        print(powerstatus)
        return powerstatus