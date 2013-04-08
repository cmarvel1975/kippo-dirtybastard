from kippo.offensive.network.sshlogin import SSHLogin

class TryPasswd(object):
    def __init__(self, clientip,  password):
        self.clientip = clientip
        self.password = password

    def start(self):
        username = "root"
        # Try these details
        SSHLogin(self.clientip, username,  self.password)
