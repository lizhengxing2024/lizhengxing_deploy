import subprocess

from base import *

MAVEN_CMD_PATH = r'D:\Software\apache-maven-3.5.0\bin\mvn.cmd'
MAVEN_CONFIG_PATH = r'D:\Software\apache-maven-3.5.0\conf\settings.xml'

LOCAL_JAR_PATH = r'D:\lizhengxing_manage\ruoyi-admin\target\ruoyi-admin.jar'

REMOTE_JAR_PATH = '/home/lizhengxing_manage/ruoyi-admin.jar'

if __name__ == '__main__':
    subprocess.run([MAVEN_CMD_PATH, '-s', MAVEN_CONFIG_PATH, 'clean', 'package'], cwd=r'D:\lizhengxing_manage')
    kill9('ruoyi-admin')
    sftp_upload(LOCAL_JAR_PATH, REMOTE_JAR_PATH)
    print('starting up ...')
    ssh_exec('/home/lizhengxing_manage/', '(nohup java -Xms500m -Xmx500m -jar ruoyi-admin.jar --server.port=8888  > ruoyi-admin.log 2>&1 &) && sleep 10')
    tail('/home/lizhengxing_manage/ruoyi-admin.log', 500)
