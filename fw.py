import sys
import subprocess
import logging

def confFw():
	lxc = 'sudo lxc-attach -n fw --clear-env -- bash -c '
	subprocess.call("sudo cp fw.fw /var/lib/lxc/fw/rootfs/root", shell = True)
	subprocess.call(lxc + " \"chmod +x /root/fw.fw\"", shell = True)
	subprocess.call(lxc + " \"/root/fw.fw\"", shell = True)
	subprocess.call(lxc + " \" rm /root/fw.fw\"", shell = True)
