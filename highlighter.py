import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

dataset = 'test_dataset'
for filename in os.listdir(dataset):
    code = open(f'{dataset}/{filename}', 'r').read()
    text = highlight(code, PythonLexer(), HtmlFormatter(full=True, style='colorful'))
    open(f'highlited_dataset/{filename.replace("py", "jpg")}', 'w').write(text)

