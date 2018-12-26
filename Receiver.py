
# this is the receiver base class.  not yet needed to make your own receiver class
class receiver:

    def __init__(self, ip):
        print("I'm here")

    def change_source(self, source):
        print("changing source to " + source)
