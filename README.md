Kippo-DirtyBastard
==================

An 'offensive' fork of the Kippo honeypot (https://code.google.com/p/kippo/). A strike-back honeypot of dubious legal, and moral, status.

Kippo-DirtyBastard requires minimal interaction from the host, setup and forget. Watch attackers connect and turn over their root access.

Features
--------

So far the feature list is short as I've just gotten going with this but:
* If the attacker uses *passwd*, try this new password on their machine.
* Try account credentials added with *adduser*.
* Email alerts for any successful return fire.
* Portscan on connection (currently only when running as root...).

Planned
-------

To come:
* Slower, less-root portscans.
* Configurable portscanning options.
* Bruteforce attacker's ssh (did they get into 'their' box the same way as yours?)

Setup
-----

Follow the Kippo setup guide here: https://code.google.com/p/kippo/ 
Edit the kippo.cfg and add which commands will be automatically run once kippo-dirtybastard gets access to a remote machine.
Email alert settings can also be found in the kippo.cfg. You will be emailed the stdout of a command after it has run so it might be worth making this useful.

