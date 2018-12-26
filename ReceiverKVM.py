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
            powerstatus = r.get_power()
            print("power status = " + str(powerstatus))
            if powerstatus == 1:
                print("current source = " + r.get_source())
                r.change_source("AUX2")
            else:
                print("receiver is off")
            r.disconnect()
            print("hanging out until device disappears")
            finder.wait_for_device_disappear(0x204,0x6025)

    print("done")

if __name__ == "__main__":
    main(sys.argv)

