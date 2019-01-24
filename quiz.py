
import sys
import subprocess
import logging

def confQuiz():
  logger = logging.getLogger('quiz')
  logger.debug('quiz')

  servers = ['s1','s2','s3']
  for s in servers:
    lxc = 'sudo lxc-attach -n ' + s + ' --clear-env -- '
    lxc_bash = 'sudo lxc-attach -n ' + s + ' --clear-env -- bash -c '

    

    subprocess.call(lxc + " apt-get update" , shell = True)
    subprocess.call(lxc + " apt-get install git -y" , shell = True)
    subprocess.call(lxc + " apt-get install nodejs -y" , shell = True)
    subprocess.call(lxc + " apt-get install npm -y " , shell = True)

    #Falta enlace simbolico!!
 
    subprocess.call(lxc + " git clone https://github.com/CORE-UPM/quiz_2019.git /root/quiz_2019" , shell = True)

    cmd = "\"cd /root/quiz_2019; npm install ;npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; \""
    subprocess.call(lxc_bash + cmd, shell = True)

    logger.debug(' solo migramos la base de datos en un servidor...')
    if s == 's1':
      cmd = "\"cd /root/quiz_2019; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31:3306/quiz; npm run-script migrate_cdps; npm run-script seed_cdps; ./node_modules/forever/bin/forever start ./bin/www\""
    else:
      cmd = "\"cd /root/quiz_2019; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31:3306/quiz; ./node_modules/forever/bin/forever start ./bin/www \""
    
    subprocess.call("" + lxc_bash + cmd , shell = True)
    

    cmd = "\"cd /root/quiz_2019/public; ln -s /mnt/nas/ uploads; \""
    subprocess.call("" + lxc_bash + cmd , shell = True)

    logger.debug(' ...terminado servidor...')
