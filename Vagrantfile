# -*- mode: ruby -*-
# vi: set ft=ruby :

# Helper for boilerplate involved with setting resource limits across providers
def set_limits(box, cpus: cpus, memory: memory)
  box.vm.provider "virtualbox" do |vb|
    vb.memory = memory
    vb.cpus = cpus
  end
  
  box.vm.provider "vmware_fusion" do |vw|
    vw.vmx["memsize"] = memory
    vw.vmx["numvcpus"] = cpus
  end
end

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # Use a Debian 8.2 base box for all machines
  config.vm.box = "box-cutter/debian82"
  
  config.vm.define "default", primary: true do |box|
    # Set resource limits
    set_limits box, cpus: 1, memory: 512
    
    # Forward ports to the host machine
    box.vm.network "forwarded_port", guest: 80, host: 8080
    
    # Create a private network between the machines
    box.vm.network "private_network", ip: "10.10.10.10"
    
    # Provision using Salt
    box.vm.provision "salt" do |salt|
      salt.bootstrap_options = "-F -c /tmp -i default"
      salt.install_master = true
      salt.minion_config = "provisioning/vagrant/minion.yml"
      salt.minion_key = "provisioning/vagrant/default.pem"
      salt.minion_pub = "provisioning/vagrant/default.pub"
      salt.master_config = "provisioning/vagrant/master.yml"
      salt.seed_master = { default: salt.minion_pub }
      salt.run_highstate = true
      salt.colorize = true
    end
  end
  
  2.times do |i|
    config.vm.define "worker#{1+i}" do |box|
      set_limits box, cpus: 1, memory: 512
      box.vm.network "private_network", ip: "10.10.10.#{11+i}"
      box.vm.provision "salt" do |salt|
      salt.bootstrap_options = "-F -c /tmp -i worker#{1+i}"
      salt.minion_config = "provisioning/vagrant/minion.yml"
      salt.run_highstate = true
      salt.colorize = true
      end
    end
  end
end
