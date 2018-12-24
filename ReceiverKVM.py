import sys
import usb
import usb.core
import usb.util
import MarantzReceiver

class find_class(object):
    def __init__(self, class_):
        self._class = class_

    def __call__(self, device):
        # first, let's check the device
        if device.bDeviceClass == self._class:
            return True
        # ok, transverse all devices to find an
        # interface that matches our class
        for cfg in device:
            # find_descriptor: what's it?
            intf = usb.util.find_descriptor(
                                        cfg,
                                        bInterfaceClass=self._class
                                )
            if intf is not None:
                return True

        return False



def main(argv):
    print("yo")
    #devs = usb.core.find(find_all=1)
    devs = usb.core.find(find_all=1, custom_match=find_class(9))
    for result in devs:
        print(result)
    r = MarantzReceiver.marantz_receiver("192.168.1.131")
#    r.change_source("AUX1")
    print("done")

if __name__ == "__main__":
    main(sys.argv)

