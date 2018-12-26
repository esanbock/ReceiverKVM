import USBFinder
import wmi

class wmiusb_finder(USBFinder.usb_finder):

    def __init__(self):
        super().__init__()
        self.c = wmi.WMI()

    def enumerateall(self, poll=.2):
        wql = "Select * From Win32_USBControllerDevice"
        for item in self.c.query(wql):
            print(item.Dependent)

    def find_by_id(self, vendor, product):
        wql = "Select * From Win32_USBControllerDevice"
        for item in self.c.query(wql):
            if "DeviceID" in item.properties:
                if "VID_" + str(vendor) in item.DeviceID and "PID_" + str(product) in item.DeviceID:
                    return True
        return False
