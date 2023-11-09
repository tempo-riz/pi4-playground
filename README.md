# pi4-playground

ping pi.local

ssh pi@pi.local

sudo apt get update && sudo apt get upgrade

sudo raspi-config
3 - interface options
3 - vnc 

sudo raspi-config 
2 - display options
d5 vnc resolution

sudo raspi-config 
1- system options
s5 boot / auto login
desktop gui -> reboot

ssh pi@pi.local
get ip address: 
hostname -I