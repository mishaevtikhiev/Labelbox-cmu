import os
from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import HtmlFormatter

dataset = '/home/egor/Work/Labelbox/compressed_for_labeling/labeling_sampled_submissions/sampled_problems_1000_9999'
for filename in os.listdir(dataset):
    code = open(f'{dataset}/{filename}', 'r').read()
    text = highlight(code, CppLexer(), HtmlFormatter(full=True, style='colorful'))
    open(f'highlighted_1000_9999/{filename.replace("cpp", "txt")}', 'w').write(text)

