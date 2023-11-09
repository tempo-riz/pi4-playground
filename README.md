# pi4-playground

ping pi.local

ssh pi@pi.local

sudo su -

apt-get update && apt-get upgrade

raspi-config
3 - interface options
3 - vnc 

raspi-config 
2 - display options
d5 vnc resolution

raspi-config 
1- system options
s5 boot / auto login
desktop gui -> reboot

ssh pi@pi.local
get ip address: 
hostname -I

## Virtual Environment

create : python -m venv myenv

windows : myenv\Scripts\activate

mac/linux: source myenv/bin/activate

quit : deactivate