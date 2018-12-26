import time

# base class for usb device searching opreartions.  Currently there is a windows-specific implementation
# using WMI and a pyusb implementation that works on Mac & Linux
class usb_finder(object):

    def __init__(self):
        self.sleeptime=.2

    def wait_for_device(self,vendor,product):
        while True:
            if self.find_by_id(vendor,product):
                return True
            time.sleep(self.sleeptime)

    def wait_for_device_disappear(self,vendor,product):
        while True:
            if self.find_by_id(vendor,product) is False:
                return True
            time.sleep(self.sleeptime)
