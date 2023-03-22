import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers import JavascriptLexer
from pygments.lexers import CppLexer
from pygments.lexers import JavaLexer
from pygments.formatters import HtmlFormatter
import imgkit
import json
lexers_dict = {"js": JavascriptLexer(), "cpp": CppLexer(), "java": JavaLexer()}

dataset = 'cmu_datasets'
for filename in os.listdir(dataset):
    lang = filename[:-5].split('_')[-1]
    lexer = lexers_dict[lang]
    with open(f'{dataset}/{filename}') as f:
        code_dataset = json.load(f)
    for task in code_dataset:
        task_id = task["task_id"]
        snippets = task["sample_from"].keys()
        for snippet_number in snippets:
            code = task[snippet_number]
            snippet_number_to_int = int(snippet_number)
            text = highlight(code, lexer, HtmlFormatter(full=True, style='colorful'))
            imgkit.from_string(text, f'highlighted_dataset/{lang}/{task_id}_{snippet_number_to_int}.jpg')


