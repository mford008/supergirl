top_template_landing = open('templates/top-landing.html').read()
bottom_template = open('templates/bottom.html').read()
content = open('content/index.html').read()

index_html = top_template_landing + content + bottom_template
open('docs/index.html', 'w+').write(index_html)

top_template = open('templates/top.html').read()
# bottom_template = open('templates/bottom.html').read()
content = open('content/about.html').read()
about_html = top_template + content + bottom_template
open('docs/about.html', 'w+').write(about_html)

content = open('content/blog.html').read()
blog_html = top_template + content + bottom_template
open('docs/about.html', 'w+').write(about_html)

content = open('content/contact.html').read()
contact_html = top_template + content + bottom_template
open('docs/about.html', 'w+').write(contact_html)

content = open('content/portfolio.html').read()
portfolio_html = top_template + content + bottom_template
open('docs/portfolio.html', 'w+').write(portfolio_html)