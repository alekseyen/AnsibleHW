# How to run


```
vagrant plugin uninstall vagrant-vbguest
vagrant plugin install vagrant-vbguest --plugin-version 0.21
```



1. Create Vagrant file
2. `vagrant destroy -f && vagrant up`
3. Create machine and write IPs inside `hosts`
4. ``ansible-playbook -i ./production ./site.yml``
5. 

