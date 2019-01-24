import sys
import subprocess
import logging

def configBbdd():
	logger = logging.getLogger('bbdd')
	logger.debug(' lb.')
	
	lxc = 'sudo lxc-attach -n bbdd --clear-env -- '

	subprocess.call(lxc + "apt update ",shell = True)
	subprocess.call(lxc + "apt -y install mariadb-server",shell = True)


	subprocess.call(lxc + "sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf",shell = True)
	subprocess.call(lxc + "systemctl restart mysql",shell = True)
	subprocess.call(lxc + "mysqladmin -u root password xxxx",shell = True)

	subprocess.call(lxc + " mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\" ",shell = True)
	subprocess.call(lxc + "mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\"",shell = True)
	subprocess.call(lxc + "mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';\"",shell = True)
	subprocess.call(lxc + "mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\"",shell = True)

	subprocess.call(lxc + "mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\"",shell = True)
