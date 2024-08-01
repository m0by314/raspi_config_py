import os
import subprocess


subprocess.call(
    "python -m PyInstaller main.py "
    "--name raspi_config "
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

build_path = os.getcwd()+'/dist/raspi_config/'
os.chdir(build_path)

if os.path.isfile('_internal/ansible/inventory/hosts.json'):
    os.symlink(
        '_internal/ansible/inventory/hosts.json',
        'hosts.json'
    )

if os.path.isfile('_internal/ansible/playbooks/raspi_config_playbook.yml'):
    os.symlink(
        '_internal/ansible/playbooks/raspi_config_playbook.yml',
        'raspi_config_playbook.yml'
    )