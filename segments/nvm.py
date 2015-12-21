import getpass
import subprocess

def add_nvm_segment():
    user = getpass.getuser()
    npm_version = subprocess.check_output(['bash', '-c', 'source /home/%s/.nvm/nvm.sh && nvm version' % user]).strip()
    if npm_version:
        powerline.append(' %s ' % npm_version, Color.JOBS_FG, Color.HOSTNAME_BG)

add_nvm_segment()
