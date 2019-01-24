import sys
import subprocess
import logging
import bbdd
import quiz
import fw
import gluster




logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('Global')
logger.debug('Configurando bbdd.')

bbdd.configBbdd()

logger = logging.getLogger('Global')
logger.debug('Terminada bbdd.')

logger = logging.getLogger('Global')
logger.debug('Configurando gluster')

gluster.confGluster()

logger = logging.getLogger('Global')
logger.debug('Terminada gluster.')

logger = logging.getLogger('Global')
logger.debug('Configurando quiz')

quiz.confQuiz()

logger = logging.getLogger('Global')
logger.debug('Terminada quiz.')

subprocess.call('sudo ./configLB.sh',shell=True)

fw.confFw()
