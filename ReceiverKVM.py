import sys
import MarantzReceiver
import PyUSBFinder

def main(argv):
    print("yo")

    finder = PyUSBFinder.pyusb_finder()
    finder.enumerateall()
    while True:
        print("waiting for device")
        if finder.wait_for_device(0x204,0x6025) is True:
            r = MarantzReceiver.marantz_receiver("192.168.1.131")
            print("power status = " + str(r.get_power()))
            print("current source = " + r.get_source())
            r.change_source("AUX2")
            r.disconnect()
            print("hanging out until device disappears")
            finder.wait_for_device_disappear(0x204,0x6025)

    print("done")

if __name__ == "__main__":
    main(sys.argv)

