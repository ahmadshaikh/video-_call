#!c:\users\shaik\appdata\local\programs\python\python37\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyngrok==4.1.5','console_scripts','pyngrok'
__requires__ = 'pyngrok==4.1.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyngrok==4.1.5', 'console_scripts', 'pyngrok')()
    )
