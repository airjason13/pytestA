import sys,os

from scapy.all import *

if os.geteuid() != 0:
    print("This need to be a root!")
    sys.exit()

if len(sys.argv) < 2:
    print("Please Use %s x.x.x.x" ,(sys.argv[0]));