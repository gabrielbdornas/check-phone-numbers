import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.', '.env'))

for name, value in os.environ.items():
    if name.split('_')[0] == 'CHECK':
    	print("{0}: {1}".format(name, value))