# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
	config.vm.define "lb" do |lb|
		lb.vm.box = "ubuntu/trusty64"
		lb.vm.network "private_network", ip: "192.168.50.10"
	end
	config.vm.define "node1" do |node1|
		node1.vm.box = "ubuntu/trusty64"
		node1.vm.network "private_network", ip: "192.168.50.11"
	end
	config.vm.define "node2" do |node2|
		node2.vm.box = "ubuntu/trusty64"
		node2.vm.network "private_network", ip: "192.168.50.12"
	end
	config.vm.define "node3" do |node3|
		node3.vm.box = "ubuntu/trusty64"
		node3.vm.network "private_network", ip: "192.168.50.13"
	end
end
