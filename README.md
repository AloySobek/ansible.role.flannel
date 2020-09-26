Role Name
=========

This role installing and configuring flannel overlay network as linux service ( starting and enabling it )

Requirements
------------

Actually flannel network config is putting to etcd_v3 cluster but flannel does not support it, so you need to put this config manually in etcd_v2 ( you may ask - but why you put this config anyway? Well... i'm just hoping that flannel will be use etcd_v3 in the future )

Role Variables
--------------

- state: 'install', 'uninstall'
- version: version of flannel to download
- flannel_args: just copy of terminal flannel flags, see example

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
        network_config: |
          {
            "Network": "10.10.0.0/16",
            "SubnetLen": 24,
            "Backend": {
              "Type": "vxlan"
            }
          }
        etcd_cafile: "/path/to/ca-cert"
        etcd_certfile: "/path/to/cert"
        etcd_keyfile: "/path/to/cert-key""
        etcd_endpoints: "https://localhost:2379"
        ip_masq: true

License
-------

MIT
