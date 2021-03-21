#! /bin/bash

pwd
ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
ansible-playbook -i inventory.yaml playbook.yaml