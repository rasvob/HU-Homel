import sys
from markdown2 import Markdown

with open(f'{sys.argv[1]}.html', 'w', encoding="utf-8") as output_file:
    with open(f'{sys.argv[1]}.md', 'r', encoding="utf-8") as input_file:
        with open('template.dev.html', 'r', encoding="utf-8") as template_file:
            content = str(Markdown().convert(input_file.read()))
            template = str(template_file.read())
            res = template.replace('#CONTENT#', content)
            output_file.write(res)
            print(f'{sys.argv[1]} render  OK')