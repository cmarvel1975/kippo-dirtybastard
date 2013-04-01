from paramiko import SSHClient, AutoAddPolicy
import threading

class TryPasswd(object):
    def __init__(self, clientip,  password):
        self.clientip = clientip
        self.password = password
        
        print "hello from TRYPASSWD"

    def start(self):
        print "Starting with ip:password ->",  self.clientip + ":" + self.password
        

        # Launch login thread
        threading.Thread(target=loginThread, args=(self.clientip, self.password)).start()
        print "LOGIN THREAD LAUCHED."
        
        

# function outside of TryPasswd as I might make it a seperate class if more logging in is going to happen.
def loginThread(clientip,  password):
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        
        try:
            client.connect(hostname=clientip,  username="root",  password=password)
        except:   
            print "Authentication failed for root@" + clientip + " (" + password + ")"
            return
            
            
        print "SUCCESS! Running command: "
        stdin, stdout, stderr = client.exec_command('mkdir TESTDIR')
        stdin, stdout, stderr = client.exec_command('ls -lah')
    
        print "stdout:",  stdout.readlines(),  "stderr", stderr.readlines()
