Python script to switch meross smart plugs on/off.
Add your credentials to credentials.conf and use it like this:

from subprocess import Popen
p = Popen("/usr/bin/python3 meross_smart_plug.py -P luefter -off", shell=True)
p.wait()

