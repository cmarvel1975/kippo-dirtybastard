Kippo-DirtyBastard
==================

An 'offensive' fork of the Kippo honeypot (https://code.google.com/p/kippo/). A strike-back honeypot of dubious legal, and moral, status.

Kippo-DirtyBastard requires minimal interaction from the host, setup and forget. Watch attackers connect and turn over their root access.

Features
--------

So far the feature list is short as I've just gotten going with this but:
* If the attacker uses *passwd*, try this new password on their machine.

Planned
-------

To come:
* Try *adduser* details on remote machine.
* Vuln-scanning a host on connection.
* Bruteforce attacker's ssh. 
* Metasploit integration (how much of this can we automate?)
* Email alerts for any successful return fire.

Setup
-----

Follow the Kippo setup guide here: https://code.google.com/p/kippo/ Edit the kippo.cfg and add which commands will be automatically run once kippo-dirtybastard gets access to a remote machine.

