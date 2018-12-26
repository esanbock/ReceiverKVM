import sys
import MarantzReceiver
import PyUSBFinder
import WMIUSBFinder
from optparse import OptionParser,  OptionGroup

def main(argv):
    print("yo")

    options, args = processCommandLine(argv)
    hostname = args[0]
    productid = int(args[1], 0)
    vendorid = int(args[2], 0)
    rsource = args[3]

    #if Windows, use WMI instead of PyUSB
    if sys.platform == "win32":
        finder = WMIUSBFinder.wmiusb_finder()
    else:
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
                r.change_source(rsource)
            else:
                print("receiver is off")
            r.disconnect()
            print("hanging out until device disappears")
            finder.wait_for_device_disappear(productid,vendorid)

    print("done")

def processCommandLine(argv):
    parser = OptionParser("ReceiverKVM <receiveraddress> <vendorid> <productid> <receiversource>")

    options, args = parser.parse_args()

    if len(args) != 4:
                parser.print_help()
                parser.error("invalid number of arguments")

    return options, args

if __name__ == "__main__":
    main(sys.argv)

