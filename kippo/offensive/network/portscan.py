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
        nm = nmap.PortScanner()
        
        nmapArgs = config().get('dirtybastard',  'nmap_args')[1:-1] # Remove quotes
        print "Running portscan at %s with arguments: %s" % (self.clientip, nmapArgs)
        
        try:
            r = nm.scan(self.clientip, arguments=nmapArgs)
        except nmap.PortScannerError:
            print "!!! PortScan error. Did you request a scan type that requires root?"
            return
            
        openTcpPorts = []
        openUdpPorts = []
        try:
            for port in nm[self.clientip]['tcp'].keys():
                openTcpPorts.append(port)
        except KeyError:
            pass
            
        try:
            for port in nm[self.clientip]['udp'].keys():
                openUdpPorts.append(port)
        except KeyError:
            pass
        
        resultsString = ""
        for port in openTcpPorts:
            resultsString += "TCP Port open: %s\n" % (port)
            
            portInfo = nm[self.clientip]['tcp'][port]
            for key in portInfo:
                resultsString += "\t - %s: %s\n" % (key,  portInfo[key])
                
        for port in openUdpPorts:
            resultsString += "UDP Port open: %s\n" % (port)
            
            portInfo = nm[self.clientip]['udp'][port]
            for key in portInfo:
                resultsString += "\t - %s: %s\n" % (key,  portInfo[key])
            
            
        print resultsString
        
        sendEmail('Port scan results ' + self.clientip,  resultsString)

