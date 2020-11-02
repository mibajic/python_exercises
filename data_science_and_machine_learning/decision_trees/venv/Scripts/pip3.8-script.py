#!C:\Users\mbajic\Documents\python\data_science_and_machine_learning\decision_trees\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==20.3b1','console_scripts','pip3.8'
__requires__ = 'pip==20.3b1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==20.3b1', 'console_scripts', 'pip3.8')()
    )
