Kippo-DirtyBastard
==================

An 'offensive' fork of the Kippo honeypot (https://code.google.com/p/kippo/). A strike-back honeypot of dubious legal, and moral, status.

Kippo-DirtyBastard requires minimal interaction from the host, setup and forget. Watch attackers connect and turn over their root access.

Features
--------

Here are the features so far:
* If the attacker uses *passwd*, try this new password on their machine.
* Try account credentials added with *adduser*.
* Email alerts for any successful return fire.
* Portscan on connection.
* Bruteforce attacker's SSH with Hydra (did they get into 'their' box the same way as yours?)
Let me know if you have any suggestions for anything.

Planned
-------

To come:
* Better portscanning options.
* Some actual error checking.

Setup
-----

Follow the Kippo setup guide here: https://code.google.com/p/kippo/ 

Edit the kippo.cfg and add which commands will be automatically run once kippo-dirtybastard gets access to a remote machine.

Email alert settings can also be found in the kippo.cfg. If kippo-dirtybastard logs in successfully anywhere, you'll be emailed the stdout afterwards, keep this in mind when writing the command in the cfg file.

Requires nmap and Hydra for portscanning and bruteforcing features respectively.
