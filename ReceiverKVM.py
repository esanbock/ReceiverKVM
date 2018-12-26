import sys
import MarantzReceiver
import PyUSBFinder

def main(argv):
    print("yo")

    finder = PyUSBFinder.pyusb_finder()
    finder.enumerateall()
    while True:
        if finder.wait_for_device(0x1050,0x0403) is True:
            r = MarantzReceiver.marantz_receiver("192.168.1.131")
            print("power status = " + str(r.get_power()))
            print("current source = " + r.get_source())
            r.change_source("AUX2")
            finder.wait_for_device_disappear()

    print("done")

if __name__ == "__main__":
    main(sys.argv)

