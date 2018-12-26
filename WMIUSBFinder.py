import USBFinder
import wmi

# this class uses WMI functionality to find the USB device.  Widnows-specific
class wmiusb_finder(USBFinder.usb_finder):

    def __init__(self):
        super().__init__()
        self.c = wmi.WMI()

    def enumerateall(self, poll=.2):
        wql = "Select * From Win32_USBControllerDevice"
        for item in self.c.query(wql):
            print(item.Dependent)

    def find_by_id(self, vendor, product):
        vendorhex = format(vendor,'x')
        producthex = format(product,'x')
        wql = "select * from Win32_PNPEntity Where deviceid Like '%USB\\VID_" + vendorhex + "&pid_" + producthex + "%'"
        items = self.c.query(wql)
        if len(items) > 0:
            return True
        return False
