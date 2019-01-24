from subprocess import call
import sys
import os
call("touch /etc/haproxy/haproxy.cfg.tmp", shell = True)
call("sudo chmod 777 /etc/haproxy/haproxy.cfg.tmp", shell = True)
f=open('/etc/haproxy/haproxy.cfg')
n=open('/etc/haproxy/haproxy.cfg.tmp', 'w')

for line in f:
    fields = line.strip().split()
    if len(fields) > 0 :
        if fields[0] == 'errorfile':
            if fields[1] == "504":
                n.write(line)
                n.write("frontend lb\nbind *:80\nmode http\ndefault_backend webservers\nbackend webservers\nmode http\nbalance roundrobin\nserver s1 20.2.3.11:3000 check\nserver s2 20.2.3.12:3000 check\nserver s3 20.2.3.13:3000 check\n")
                continue
    n.write(line)
f.close()
n.close()

os.remove("/etc/haproxy/haproxy.cfg")
os.rename("/etc/haproxy/haproxy.cfg.tmp", "/etc/haproxy/haproxy.cfg")

call("sudo service haproxy restart ",shell=True)

