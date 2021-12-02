# How ot run

1. Crete Vms(2 linux machine) 

   `vagrant destroy -f && vagrant up`

   (`vagrant destroy -f && IS_HOME="true" vagrant up` - if run from root)
2. Check if servers is available:

    ```ansible all -m ping```

    password – vagrant

3. Run app:

    `ansible-playbook nginx.yml`

    (password – vagrant)

4. Check servers correctly working:

    `curl vagrant@10.211.100.101/service_data` (change on yours ip)

# Remarks
1. nginx/vars/main.yml
   1. `file_name` – file we should write
   2. `host_name` – api we can curl. Others will return 404
2. For work with `Centos` vm, pls install vbguest plugin:

```
vagrant plugin uninstall vagrant-vbguest
vagrant plugin install vagrant-vbguest --plugin-version 0.21
```

