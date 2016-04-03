# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
	N = 4
	(1..N).each do |machine_id|
  	config.vm.define "node#{machine_id}" do |node|
			node.vm.box = "ubuntu/trusty64"
    	node.vm.hostname = "node#{machine_id}"
    	node.vm.network "private_network", ip: "192.168.77.#{20+machine_id}"
			# Set port forward for the load balancer	
			if machine_id == 1
				node.vm.network "forwarded_port", guest: 80, host: 6666
			end
    	# Only execute the Ansible provisioner once,
    	# when all the nodes are up and ready.
    	if machine_id == N
      	node.vm.provision :ansible do |ansible|
        	# Disable default limit to connect to all the machines
        	ansible.limit = "all"
      		ansible.playbook = "ansible/setup.yml"
      	end
    	end
  	end
	end
end
