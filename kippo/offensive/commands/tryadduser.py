from kippo.offensive.network.sshlogin import SSHLogin

class TryAdduser(object):
    def __init__(self, clientip, username,  password):
        self.clientip = clientip
        self.username = username
        self.password = password

    def start(self):
        SSHLogin(self.clientip, self.username,  self.password)

