import Receiver
import Marantz

class marantz_receiver(Receiver.receiver):

    def __init__(self, ip):
        print("connecting...")
        ip = Marantz.IP(ip)
        ip.test()

    def change_source(self, source):
        print("changing source to " + source)
