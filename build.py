import os
import subprocess


subprocess.call(
    "python -m PyInstaller main.py "
    "--name raspi_config_py "
    "--add-data ansible/:ansible/ "
    "--collect-all ansible  "
    "--collect-all ansible_runner "
    "--add-binary venv/bin/ansible-playbook:./bin "
    "-y "
    "-c ",
    cwd=os.getcwd(),
    shell=True,
    stdin=subprocess.PIPE,
)

if os.path.isfile(os.getcwd()+'/dist/raspi_config_py/_internal/ansible/inventory/hosts.json'):
    os.symlink(
        os.getcwd()+'/dist/raspi_config_py/_internal/ansible/inventory/hosts.json',
        os.getcwd() + '/dist/raspi_config_py/hosts.json'
    )

if os.path.isfile(os.getcwd()+'/dist/raspi_config_py/_internal/ansible/playbooks/raspi_config_playbook.yml'):
    os.symlink(
        os.getcwd()+'/dist/raspi_config_py/_internal/ansible/playbooks/raspi_config_playbook.yml',
        os.getcwd() + '/dist/raspi_config_py/raspi_config_playbook.yml'
    )