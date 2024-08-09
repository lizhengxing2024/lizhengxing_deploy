from base import *

if __name__ == '__main__':
    print('starting up ...')
    kill9('ruoyi-admin')
    ssh_exec('/home/lizhengxing_manage/', '(nohup java -Xms500m -Xmx500m -jar ruoyi-admin.jar --server.port=8888  > ruoyi-admin.log 2>&1 &) && sleep 10')
    tail('/home/lizhengxing_manage/ruoyi-admin.log', 500)