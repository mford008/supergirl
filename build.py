def main():

    pages = [
        {
        'filename': 'content/about.html',
        'output_filename': 'docs/about.html',
        },
        {
        'filename': 'content/blog.html',
        'output_filename': 'docs/blog.html',
        },
        {
        'filename': 'content/contact.html',
        'output_filename': 'docs/contact.html',
        },
        {
        'filename': 'content/portfolio.html',
        'output_filename': 'docs/portfolio.html',
        }
    ]

    for x in pages:
        template = open('templates/base.html').read()
        content = open(x['filename']).read()
        finished_page = template.replace('{{content}}', content)
        open(x['output_filename'], 'w+').write(finished_page)
        
    # top_template_landing = open('templates/top-landing.html').read()
    # bottom_template_landing = open('templates/bottom-landing.html').read()
    # content = open('content/index.html').read()
    # index_html = top_template_landing + content + bottom_template_landing
    # open('docs/index.html', 'w+').write(index_html)
    #
    # for x in pages:
    #     top_template = open('templates/top.html').read() #still need to establish top and bottom templates
    #     bottom_template = open('templates/bottom.html').read()
    #     content = open(x['filename']).read()
    #     newpage = top_template + content + bottom_template
    #     open(x['output_filename'], 'w+').write(newpage)
    #     print('success!')

if __name__ == '__main__':
    main()
