from paramiko import SSHClient, AutoAddPolicy
import threading

class TryPasswd(object):
    def __init__(self, clientip,  password):
        self.clientip = clientip
        self.password = password

    def start(self):
        # Launch login thread
        threading.Thread(target=loginThread, args=(self.clientip, self.password)).start()
        print "LOGIN THREAD LAUCHED."


# function outside of TryPasswd as I might make it a seperate class if more 'logging in' is going to happen.
def loginThread(clientip,  password):
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
    
        print "Attempting login with root@" + clientip +" (" + password + ")"
        
        try:
            client.connect(hostname=clientip,  username="root",  password=password)
        except:   
            print "Authentication failed for root@" + clientip + " (" + password + ")"
            return
            
        print "SUCCESS! Running commands. "
        stdin, stdout, stderr = client.exec_command('mkdir HELLO')
        stdin, stdout, stderr = client.exec_command('ls -lah')
    
        print "stdout:"
        for line in stdout.readlines():
            print line.strip()
