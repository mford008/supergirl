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
        # {
        # 'filename': 'content/index.html',
        # 'title': 'Index',
        # },
        {
        'filename': 'content/portfolio.html',
        'output_filename': 'docs/portfolio.html',
        }
    ]


# Leave this code alone and out of for loop for now
    # top_template_landing = open('templates/top-landing.html').read()
    # bottom_template_landing = open('templates/bottom-landing.html').read()
    # content = open('content/index.html').read()
    # index_html = top_template_landing + content + bottom_template_landing
    # open('docs/index.html', 'w+').write(index_html)

    for x in pages:
        top_template = open('templates/top.html').read() #still need to establish top and bottom templates
        bottom_template = open('templates/bottom.html').read()
        content = open(x['filename']).read()
        # {title}_html = top_template + {filename} + bottom_template #use title and filename from pages list
        # open('docs/{title}.html', 'w+').write({title}_html) #need a write command for docs
        # print(x['filename'])
        # print(x['title'])
        newpage = top_template + content + bottom_template
        open("x[output_filename]", 'w+').write(newpage)
    # top_template = open('templates/top.html').read()
    # bottom_template = open('templates/bottom.html').read()
    # content = open('content/about.html').read()
    # about_html = top_template + content + bottom_template
    # open('docs/about.html', 'w+').write(about_html)
    #
    # content = open('content/blog.html').read()
    # blog_html = top_template + content + bottom_template
    # open('docs/blog.html', 'w+').write(blog_html)
    #
    # content = open('content/contact.html').read()
    # contact_html = top_template + content + bottom_template
    # open('docs/contact.html', 'w+').write(contact_html)
    #
    # content = open('content/portfolio.html').read()
    # portfolio_html = top_template + content + bottom_template
    # open('docs/portfolio.html', 'w+').write(portfolio_html)

if __name__ == '__main__':
    main()
