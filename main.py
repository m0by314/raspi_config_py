import os

import ansible_runner

from pathlib import Path

workdir = str(os.path.dirname(Path(__file__).resolve()))

os.environ["PATH"] += os.pathsep + workdir + "/bin"  # Add bin path for compiled application

if __name__ == '__main__':
    ret = ansible_runner.run(
        inventory=Path(workdir, "ansible/inventory/hosts.json").as_posix(),
        playbook=Path(workdir, 'ansible/playbooks/raspi_config_playbook.yml').as_posix()
    )

    print("{}: {}".format(ret.status, ret.rc))
    print("'Final' status:")
    print(ret.stats)
