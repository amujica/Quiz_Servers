import sys
import subprocess
import logging

def confGluster():
	logger = logging.getLogger('gluster')
	logger.debug(' configurando cluster desde nas1')

	logger.debug('asignamos las ips')
	ips = ['20.2.4.21','20.2.4.22','20.2.4.23']
	maquinas = ['nas1','nas2','nas3']
	einkomen = 'sudo lxc-attach -n ' + maquinas[0] + ' --clear-env -- '

	for c in ips:
		subprocess.call(einkomen + "gluster peer probe "+c , shell = True)
	logger.debug('...comprobando...')
	subprocess.call(einkomen + "gluster peer status " , shell = True)
	logger.debug('asignamos volumenes')	
	subprocess.call(einkomen + "gluster volume create nas replica 3 transport tcp 20.2.4.21:/nas 20.2.4.22:/nas 20.2.4.23:/nas force " , shell = True)
	subprocess.call(einkomen + "gluster volume start nas" , shell = True)
	subprocess.call(einkomen + "gluster volume set nas network.ping-timeout 5" , shell = True)

	servers = ['s1','s2','s3']
	for s in servers:
		einkomen2 = 'sudo lxc-attach -n ' + s + ' --clear-env -- '

		subprocess.call(einkomen2 + " mkdir /mnt/nas " , shell = True)
		subprocess.call(einkomen2 + " mount -t glusterfs 20.2.4.21:/nas /mnt/nas " , shell = True)

	logger.debug(' ...comprobando...')

	subprocess.call(einkomen + " gluster volume info " , shell = True)
