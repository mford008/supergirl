import glob
import os
from jinja2 import Template
import markdown

site = {
    'base': 'templates/base.html',
    'pages': [],
}
landing = {
    'base': 'templates/base-landing.html',
    'pages': [],
}
def main():
    all_content_files = glob.glob('content/*.html')
    landing_file = glob.glob('landing/*.html')
    # establishing list
    for page in all_content_files:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        collect(page, file_name, name_only)
    #using list
    for page in site['pages']:
        template(['filename']) #what needs to go in place of filename?
        # convert(???)
        open(site['pages']['filepath'], 'w+').write(site['pages']['templated_content'])
    for page in landing_file:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        collect_landing(page, file_name, name_only)
        # convert(???)
        template_landing(page)
        open(landing['pages']['filepath'], 'w+').write(landing['pages']['templated_content'])

def collect(page, file_name, name_only):
    site['pages'].append({
        'filename': str(page),
        'filepath': 'docs/'+str(file_name),
        'title': 'Maddy Ford - ' + name_only,
    })
def collect_landing(page, file_name, name_only):
    landing['pages'] = {
        'filename': str(page),
        'filepath': 'docs/'+str(file_name),
        'title': 'Maddy Ford'
    }

def template(page):
    content_html = open(['filename']).read() #what needs to go in place of filename?
    template_html = open(site['base']).read()
    template = Template(template_html)
    finished_page = template.render(
        title = site['pages']['title'],
        content = content_html,
        filepath = site['pages']['filepath'],
        pages = site['pages'],
    )
    site['pages'].update({'templated_content': finished_page})
def template_landing(page):
    content_html = open(page).read()
    template_html = open(landing['base']).read()
    template = Template(template_html)
    finished_page = template.render(
        title = landing['pages']['title'],
        content = content_html,
    )
    landing['pages'].update({'templated_content': finished_page})

if __name__ == '__main__':
    main()
#converting markdown
def convert(page):
for page in pages:
    md = markdown.Markdown(extensions = 'markdown.extensions.meta')
    data = page
    html = md.convert(data)
    title = md.Meta['title']
    author = md.Meta['author']
