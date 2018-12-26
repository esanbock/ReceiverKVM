import sys
import MarantzReceiver
import PyUSBFinder
from optparse import OptionParser,  OptionGroup

if sys.platform == "win32":
    import WMIUSBFinder

def main(argv):
    print("yo")

    options, args = processCommandLine(argv)
    receivertype = args[0]
    hostname = args[1]
    receiversource = args[2]
    productid = int(args[3], 0)
    vendorid = int(args[4], 0)

    #if Windows, use WMI instead of PyUSB
    if sys.platform == "win32":
        finder = WMIUSBFinder.wmiusb_finder()
    else:
        finder = PyUSBFinder.pyusb_finder()

    # dump all devices.  Informational, should probably be its own command line parameter
    finder.enumerateall()

    # Wait for the USB trigger device to appear (KVM switch to me), check the power status
    # to make sure that the receiver is on.  If so, change the receiver source
    # If this is successful, then wait for the device to disappear (KVM switch away)  and start again
    while True:
        print("waiting for device to appear")
        if finder.wait_for_device(productid,vendorid) is True:
            r = makeReceiver(receivertype,hostname)
            powerstatus = r.get_power()
            print("power status = " + str(powerstatus))
            if powerstatus == 1:
                print("current source = " + r.get_source())
                r.change_source(receiversource)
            else:
                print("receiver is off")
            r.disconnect()
            print("hanging out until device disappears")
            finder.wait_for_device_disappear(productid,vendorid)

def processCommandLine(argv):
    parser = OptionParser("ReceiverKVM <receivertype> <receiveraddress> <receiversource> <usbvendorid> <usbproductid> ")

    options, args = parser.parse_args()

    if len(args) != 5:
                parser.print_help()
                parser.error("invalid number of arguments")

    return options, args

def makeReceiver(type, hostname):
    if "marantz" in type.lower():
        return MarantzReceiver.marantz_receiver(hostname)

    raise Exception("unsupported receiver type.  Must pass in marantz")

if __name__ == "__main__":
    main(sys.argv)

