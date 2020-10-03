ansible.role.flannel
=========

This role installing and configuring flannel overlay network as linux service ( starting and enabling it )

Requirements
------------

Actually flannel network config is putting to etcd_v3 cluster but flannel does not support it, so you need to put this config manually in etcd_v2 ( you may ask - but why you put this config anyway? Well... i'm just hoping that flannel will be use etcd_v3 in the future )

Role Variables
--------------

- state: 'install', 'uninstall'
- version: version of flannel to download
- service_file: path to service file
- network_config_file: path to network config file
- etcd_prefix: for example "/coreos.com/network"
- etcd_cafile: path to ca file
- etcd_certfile: path to cert file
- etcd_endpoints: etcd endpoints comma separated
- etcd_keyfile: path to key file

Dependencies
------------

- ansible.community 'etcd3' module
- ansible.role.etcd (By AloySobek for example)

Example Playbook
----------------

    - name: how to install flannel - example
      hosts: example
      roles:
         - ansible.role.flannel
      vars:
        state: install
        version: "0.12.0"
        service_file: "./services/flannel.service"
        network_config_file: "./configs/config.json"
        etcd_cafile: "/path/to/ca-cert"
        etcd_certfile: "/path/to/cert"
        etcd_keyfile: "/path/to/cert-key""
        etcd_endpoints: "https://localhost:2379"

License
-------

MIT
