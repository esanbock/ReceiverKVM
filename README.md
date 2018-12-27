# ReceiverKVM
Turn an a/v receiver and a USB-switch into a KVM.  All of the high-end A/V features, none of the high-end KVM price.  A USB switch costs $10. You will need an A/V receiver of some sort.  This works with my Maratnz receiver.  Will add Onkyo next.  Feel free to submit code for your own receivers.

#On computer #1:
./ReceiverKVM marantz 192.168.1.131 GAME 0x4f2 0x0833

#On computer #2
./ReceiverKVM marantz 192.168.1.131 "SAT/CBL" 0x4f2 0x0833

where 0x4f2 and 0x0833 are manufacturer and product IDs of the USB device that you want to trigger the switch.  In this case, I'm using an Amazon Basics keyboard.  To find these identefiers use lsusb in linux.

Any time the KVM switches to another source, the computer that sees the keyboard (or your chosen device) will connect to the receiver and change the video & audio source so that you don't have to push two buttons, like a complete savage.
