# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
    # vm image
    config.vm.box = "alvistack/ubuntu-22.04"

    # via 127.0.0.1 to disable public access
    # - Nginx
    config.vm.network "forwarded_port", guest: 80, host: 80, host_ip: "127.0.0.1"
    # - Docker
    config.vm.network "forwarded_port", guest: 2375, host: 2375, host_ip: "127.0.0.1"
    # - WAS
    config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"
    # - Elastic
    config.vm.network "forwarded_port", guest: 5601, host: 5601, host_ip: "127.0.0.1"
    config.vm.network "forwarded_port", guest: 9000, host: 9000, host_ip: "127.0.0.1", auto_crrect: true
    config.vm.network "forwarded_port", guest: 9200, host: 9200, host_ip: "127.0.0.1"

    # vm spec
    config.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = "8192"
    end

    # boot command
    config.vm.provision "shell", inline: <<-SHELL
      apt-get update
    SHELL
  end
