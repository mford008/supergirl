import glob
import os
from jinja2 import Template
import markdown

pages = []
landing = {
    'base': 'templates/base-landing.html',
    'page': 'landing/index.html',
}

def main():
    all_content_files = glob.glob('content/*.md')
    landing_content_file = glob.glob(landing['page'])
    for page in all_content_files:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        convert(page)
        append(file_name, name_only)
    for page in pages:
        content_html = open(page['filepath']).read()
        template_html = open('templates/base.html').read()
        template = Template(template_html)
        finished_page = template.render(
            title = page['title'],
            content = content_html,
            filepath = page['output_filepath'],
        )
        open(page['output_filepath'], 'w+').write(finished_page)

def append(file_name, name_only):
    pages.append({
        'filepath': 'content/'+str(file_name),
        'filename': file_name,
        'output_filepath': 'docs/'+str(name_only) + '.html',
        'title': 'Maddy Ford - ' + name_only,
    })

def convert(page):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    md_content = open(page).read()
    html = md.convert(md_content)
    return html


if __name__ == '__main__':
    main()
