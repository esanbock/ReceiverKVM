import wmi

class wmiusb_finder(object):

    def __init__(self):
        self.c = wmi.WMI()

    def enumerateall(self, poll=.2):
        wql = "Select * From Win32_USBControllerDevice"
        for item in self.c.query(wql):
            print(item.Dependent)
