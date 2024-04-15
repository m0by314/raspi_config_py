import os
import ansible_runner

from pathlib import Path


"""
sur Mac installer les certificat ssl
/Applications/Python\ 3.11/Install\ Certificates.command ; exit;
"""

if __name__ == '__main__':
    ret = ansible_runner.run(
        inventory=Path(os.getcwd(), "hosts.json").as_posix(),
        playbook=Path(os.getcwd(), 'raspi_config_playbook.yml').as_posix()
    )

    print("{}: {}".format(ret.status, ret.rc))

    print("'Final' status:")
    print(ret.stats)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
