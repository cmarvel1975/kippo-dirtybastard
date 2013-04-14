import threading
import nmap

from kippo.core.config import config
from kippo.core.sendemail import sendEmail

class PortScan(object):
    def __init__(self, clientip):
        self.clientip = clientip
        
        performPortscan = config().getboolean('dirtybastard',  'port_scan')
        if performPortscan:
            threading.Thread(target=self.scanThread).start()

    def scanThread(self):
        nmapCommandArgs = "-sS"

        nm = nmap.PortScanner()
        
        print "Running portscan at %s with arguments: %s" % (self.clientip, nmapCommandArgs)
        
        try:
            r = nm.scan(self.clientip, arguments=nmapCommandArgs)
        except nmap.PortScannerError:
            print "!!! PortScan error. Did you request a scan type that requires root?"
            return
            
        scanOpen = []
        try:
            for port in nm[self.clientip]['tcp'].keys():
                scanOpen.append(port)
        except KeyError:
            pass
            
        resultsString = "Results for " + self.clientip + ", open TCP: " + str(list(set(scanOpen)))
        print resultsString
        
        sendEmail('Port scan results',  resultsString)

