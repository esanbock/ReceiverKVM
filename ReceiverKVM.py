import sys
import MarantzReceiver
import PyUSBFinder
from optparse import OptionParser,  OptionGroup

def main(argv):
    print("yo")

    options, args = processCommandLine(argv)
    hostname = args[0]
    productid = int(args[1], 0)
    vendorid = int(args[2], 0)

    finder = PyUSBFinder.pyusb_finder()
    finder.enumerateall()
    while True:
        print("waiting for device")
        if finder.wait_for_device(productid,vendorid) is True:
            r = MarantzReceiver.marantz_receiver(hostname)
            powerstatus = r.get_power()
            print("power status = " + str(powerstatus))
            if powerstatus == 1:
                print("current source = " + r.get_source())
                r.change_source("AUX2")
            else:
                print("receiver is off")
            r.disconnect()
            print("hanging out until device disappears")
            finder.wait_for_device_disappear(productid,vendorid)

    print("done")

def processCommandLine(argv):
    parser = OptionParser("ReceiverKVM <receiveraddress> <vendorid> <productid>")

    options, args = parser.parse_args()

    if len(args) != 3:
                parser.print_help()
                parser.error("invalid number of arguments")

    return options, args

if __name__ == "__main__":
    main(sys.argv)

