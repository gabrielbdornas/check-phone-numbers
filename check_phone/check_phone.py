import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.', '.env'))

CHECKS = {}

for key, value in os.environ.items():
  if key.split('_')[0] == 'CHECK':
    cpf = value.split(',')[0]
    companies = value.split(',')[1:]
    name = ' '.join(key.split('_')[1:])        
    CHECKS[f'{cpf}'] = {
        'name': name,
        'companies': companies,    
    }
