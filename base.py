import fabric
import webbrowser

hostname = '118.89.201.168'
username = 'root'
password = 'LiZhengXing0611,.|'

def ssh_exec(cwd, cmd):
    with fabric.Connection(host=hostname, user=username, connect_kwargs={'password': password}) as c:
        with c.cd(cwd):
            r = c.run(cmd, encoding='utf-8')
            print(r)

def sftp_upload(local_file_path, remote_file_path):
    print('uploading [%s] to [%s] ...' % (local_file_path, remote_file_path))
    with fabric.Connection(host=hostname, user=username, connect_kwargs={'password': password}) as c:
        c.put(local_file_path, remote_file_path)
    print('done.')

def tail(logfile, n):
    with fabric.Connection(host=hostname, user=username, connect_kwargs={'password': password}) as c:
        r = c.run(r'tail -n %i %s' % (n, logfile), encoding='utf-8')
        print(r)

def kill9(app):
    try:
        with fabric.Connection(host=hostname, user=username, connect_kwargs={'password': password}) as c:
            r = c.run('ps aux | grep "%s" | cut -c 9-16 | xargs kill -9' % (app), encoding='utf-8')
            print(r)
    except:
        pass

def open_browser(url):
    webbrowser.open(url)