import os
import shutil

import subprocess


subprocess.call(
    "python -m PyInstaller main.py --name raspi_config_py --noconfirm --add-data ansible/roles:ansible/roles --add-data ansible/playbooks/raspi_config_playbook.yml:. --add-data ansible/inventory/hosts.json:. -c --collect-all ansible --collect-all ansible_runner",
    cwd=os.getcwd(),
    shell=True,
)

if os.path.isfile(os.getcwd()+'/dist/raspi_config_py/_internal/raspi_config_playbook.yml'):
    shutil.move(os.getcwd()+'/dist/raspi_config_py/_internal/raspi_config_playbook.yml' , os.getcwd()+'/dist/raspi_config_py/raspi_config_playbook.yml')

if os.path.isfile(os.getcwd()+'/dist/raspi_config_py/_internal/hosts.json'):
    shutil.move(os.getcwd()+'/dist/raspi_config_py/_internal/hosts.json' , os.getcwd()+'/dist/raspi_config_py/hosts.json')