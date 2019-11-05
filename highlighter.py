import requests
import os

URL = 'http://hilite.me/api'

for filename in os.listdir('dataset'):
    fileContent = open(f'dataset/{filename}', 'r').read()
    PARAMS = {
        'code': fileContent,
        'lexer': 'c++'
    }
    r = requests.get(url = URL, params = PARAMS)
    open(f'dataset-highlighted/{filename.replace("cpp", "html")}', 'w').write(str(r.text))
