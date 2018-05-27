pages = [
    {
    'title': 'About',
    'filename': 'content/about.html',
    'output_filename': 'docs/about.html',
    },
    {
    'title': 'Blog',
    'filename': 'content/blog.html',
    'output_filename': 'docs/blog.html',
    },
    {
    'title': 'Contact',
    'filename': 'content/contact.html',
    'output_filename': 'docs/contact.html',
    },
    {
    'title': 'Portfolio',
    'filename': 'content/portfolio.html',
    'output_filename': 'docs/portfolio.html',
    }
]

def main():
    for x in pages:
        template = open('templates/base.html').read()
        content = open(x['filename']).read()
        finished_page = template.replace('{{content}}', content).replace('{{title}}', 'Maddy Ford - ' + x['title'])
        open(x['output_filename'], 'w+').write(finished_page)

        template = open('templates/base-landing.html').read()
        content = open('content/index.html').read()
        finished_landing_page = template.replace('{{content}}', content).replace('{{title}}', 'Maddy Ford')
        open('docs/index.html', 'w+').write(finished_landing_page)

if __name__ == '__main__':
    main()
