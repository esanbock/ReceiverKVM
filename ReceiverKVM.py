import sys
import MarantzReceiver
import PyUSBFinder

def main(argv):
    print("yo")

    finder = PyUSBFinder.pyusb_finder()
    finder.enumerateall()
    if finder.findbyid(0x1050,0x0403):
        r = MarantzReceiver.marantz_receiver("192.168.1.131")
        print("power status = " + str(r.get_power()))
        print("current source = " + r.get_source())

    print("done")

if __name__ == "__main__":
    main(sys.argv)

