import subprocess

from base import *

LOCAL_PROJECT_HOME = r'D:\_PRIVATE_\lizhengxing_site'
REMOTE_DEPLOY_HOME = '/home'

if __name__ == '__main__':
    subprocess.run([r'C:\Program Files\nodejs\npm.cmd', 'run', 'build'], cwd=LOCAL_PROJECT_HOME)
    subprocess.Popen(['tar', 'cf', 'lizhengxing_site.tar', 'dist'], cwd=LOCAL_PROJECT_HOME)
    ssh_exec(REMOTE_DEPLOY_HOME, 'rm -rf /home/lizhengxing_site')
    sftp_upload(r'D:\_PRIVATE_\lizhengxing_site\lizhengxing_site.tar', '/home/lizhengxing_site.tar')
    ssh_exec(REMOTE_DEPLOY_HOME, 'tar -xf lizhengxing_site.tar && mv dist lizhengxing_site && rm -rf lizhengxing_site.tar')
    print('starting up ...')
    open_browser('https://www.lizhengxing.com')