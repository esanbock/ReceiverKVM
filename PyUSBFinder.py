import usb
import usb.core
import usb.util

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

class pyusb_finder(object):
    def findbyid(self, vendor, product):
        dev = usb.core.find(idVendor=vendor, idProduct=product)
        if dev is None:
            return False
        return True

    def enumerateall(self):
        devs = usb.core.find(find_all=1)
        for result in devs:
            print(result)