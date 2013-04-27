Kippo-DirtyBastard
==================

An 'offensive' fork of the Kippo honeypot (https://code.google.com/p/kippo/). A strike-back honeypot of dubious legal, and moral, status.

Kippo-DirtyBastard requires minimal interaction from the host, setup and forget. 

Features
--------

Here are the features so far:

* If the attacker uses *passwd*, try to SSH with this password onto their machine.
* Try account credentials added with *adduser*.
* Email alerts for any successful return fire.
* Portscan on connection.
* Bruteforce attacker's SSH with Hydra (did they get into 'their' box the same way as yours?).

Let me know if you have any suggestions for anything.

Setup
-----

Follow the Kippo setup guide here: https://code.google.com/p/kippo/ 

Edit the kippo.cfg and add which commands will be automatically run once kippo-dirtybastard gets access to a remote machine.

Email alert settings can also be found in the kippo.cfg. If kippo-dirtybastard accesses anywhere, you'll be emailed the stdout afterwards, keep this in mind when writing the command in the cfg file.

Requires nmap, python-nmap and Hydra for portscanning and bruteforcing features respectively.

Disclaimer
----------

Don't actually run this. It'd probably be illegal in most places to stick it on the internet.
