# -*- mode: ruby -*-
# vi: set ft=ruby :

# CHOOSE THE DISTRO FOR COLAB VM (set the distro variable):
# - precise64
# - trusty64
# - seocam/centos-7.0

default_box = "trusty64"
if $stdin.isatty
  if Dir.glob(File.join(File.dirname("__FILE__"), '.vagrant/**/id')).empty?
    options = ["trusty64", "seocam/centos-7.0"]

    puts "Bases boxes available locally:"
    puts '------------------------------'
    system('vagrant', 'box', 'list')
    puts
    puts 'Base boxes we can provide you:'
    puts '------------------------------'
    options.each_with_index do |value, i|
      puts "[#{i + 1}] #{value}"
    end

    print "Which box to use [#{default_box}]: "
    choice = $stdin.gets.strip
    options.each_with_index do |option, i|
      if option == choice || choice.to_i == (i + 1)
        default_box = option
        puts default_box
        break
      end
    end
   end
end

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.

  config.vm.box = default_box

  directory_name = "../colab-plugins"
  Dir.mkdir(directory_name) unless File.exists?(directory_name)

  case config.vm.box
  when "precise64"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box"
  when "trusty64"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  when "seocam/centos-7.0"
    config.vm.box_url = "seocam/centos-7.0"
  end

  config.vm.provision "shell", keep_color: true, path: 'vagrant/bootstrap.sh'
  config.vm.provision "shell", privileged: false, keep_color: true, path: "vagrant/provision.sh"

  config.vm.network :forwarded_port, guest: 8000, host: 8000 # Colab (runserver)

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "../colab-plugins", "/colab-plugins"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true

    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end
end
