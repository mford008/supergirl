import glob
import os
from jinja2 import Template
import markdown

pages = []
landing = {
    'base': 'templates/base-landing.html',
    'pages': [],
}
def main():
    #grabbing all files, saving as variable
    all_content_files = glob.glob('content/*.md')
    #doing same for landing file
    landing_file = glob.glob('landing/*.html')
    # establishing list by looping through list variable
    for page in all_content_files:
        file_name = os.path.basename(page)
        # print('filename', file_name) #filename.ext
        name_only, extension = os.path.splitext(file_name)
        # print('name only', name_only) #filename
        # print('extension', extension)#.md
        #appending information to site['pages'] for each page
        collect(page, file_name, name_only) #makes a list of dictionaries
    #using list
    for page in pages:
        # print('meow', filename)
        # print('meow', [filename])
        # print('meow', ['filename'])
        print('TEST', page['filename'])
        template(page['filename']) #what needs to go in place of filename?
        # convert(???)
        open(page['filepath'], 'w+').write(page['templated_content'])
    for page in landing_file:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        collect_landing(page, file_name, name_only)
        # convert(???)
        template_landing(page)
        open(landing['pages']['filepath'], 'w+').write(landing['pages']['templated_content'])

def collect(page, file_name, name_only):
    pages.append({
        'filename': str(page),
        'filepath': 'docs/'+str(file_name),
        'title': 'Maddy Ford - ' + name_only,
    })
    # print('page', page) #filename.ext
    # print('test', site['pages']) #prints a list of dictionaries
def collect_landing(page, file_name, name_only):
    landing['pages'] = {
        'filename': str(page),
        'filepath': 'docs/'+str(file_name),
        'title': 'Maddy Ford'
    }

def template(page):
    # print(type(['filename']))
    content_html = open(page['filename']).read() #what needs to go in place of filename?
    template_html = open('templates/base.md').read()
    template = Template(template_html)
    finished_page = template.render(
        title = pages['title'],
        content = content_html,
        filepath = pages['filepath'],
        pages = pages,
    )
    pages.update({'templated_content': finished_page})
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
# def convert(page):
#     for page in pages:
#         md = markdown.Markdown(extensions = 'markdown.extensions.meta')
#         data = page
#         html = md.convert(data)
#         title = md.Meta['title']
#         author = md.Meta['author']
