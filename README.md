Nginx Loadbalancer
==================

Simple loadbalancer setup using Nginx, Ansible and Vagrant

NOTE: Tested in a debian workstation

How to run it
-------------

Clone the repository, cd into it and execute:

$ vagrant up
$ python verify.py [-n 200]

The "-n" option indicates the amount of http requests that 
you wish to run towards the loadbalancer server

NOTE: Port 6666 should be available in your system, 
otherwise just modify the Vagrantfile and use a suitable port
for your system. 
