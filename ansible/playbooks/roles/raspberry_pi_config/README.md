Ansible Role - Raspberry Pi Config
===========================

An Ansible role to configure and secure a Raspberry Pi. 

Functional with the OS Raspbian Lite, doesn't work with Raspbian Desktop

This role applies the security rules defined in the [official documentation](https://www.raspberrypi.org/documentation/configuration/security.md)


Requirements
------------

None

Role Variables
--------------

Variables are listed below along with default values:

Variable                          | Required | Default value | Description/Comment
----------------------------------| -------- | --------------| -----------
**rasp_ssh_port**                 |          | 22            | Port ssh
**SERIAL**                        |          | true          | Enable/disable shell and kernel messages on the serial connection. (enabled by default)
**CAMERA**                        |          | false         | Enable/disable the CSI camera interface
**VNC**                           |          | false         | Enable/disable the RealVNC virtual network computing server
**SPI**                           |          | false         | Enable/disable SPI interfaces and automatic loading of the SPI kernel module, needed for products such as PiFace.
**I2C**                           |          | false         | Enable/disable I2C interfaces and automatic loading of the I2C kernel module.
**ONEWIRE**                       |          | false         | Enable/disable the Dallas 1-wire interface. This is usually used for DS18B20 temperature sensors.
**RGPIO**                         |          | false         | Enable or disable remote access to the GPIO pins.
**rasp_extra_packages**           |          | []            | List of packages to install.
**rasp_firewall**                 |          | false         | Enable/disable firewall
**rasp_open_firewall_port**       |          | []            | List the ports to open

**If the firewall is activated, automatically the ssh port contained in the variable rasp_ssh_port is opened** 

**Automatic packages installed by this role**: openssh-server, logrotate, fail2ban, ufw

Dependencies
------------

None.

Example Playbook
----------------

```yaml
---
- hosts: pi
  become: true
  remote_user: pi

  vars:
    rasp_ssh_port: 2225
    rasp_extra_packages:
      - python3
      - golang
    CAMERA: true
    rasp_firewall: true
    rasp_open_firewall_port:
      - 80
      - 8080

  roles:
    - raspberry_pi_config
```

License
-------

MIT

Author Information
------------------

[m0by314](https://github.com/m0by314)
