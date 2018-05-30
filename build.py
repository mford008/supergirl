pages = [
    {
    'title': 'About',
    'headline': 'Hey, Hi, and Hello!',
    'brand': '<a class="navbar-brand" href="index.html">Maddy Ford</a>',
    'filename': 'content/about.html',
    'output_filename': 'docs/about.html',
    'active_class': 'about_me_active',
    },
    {
    'title': 'Blog',
    'headline': 'Working Title',
    'brand': '<a class="navbar-brand" href="index.html">Maddy Ford</a>',
    'filename': 'content/blog.html',
    'output_filename': 'docs/blog.html',
    'active_class': 'blog_active',
    },
    {
    'title': 'Blog Post',
    'headline': 'Working Title',
    'brand': '<a class="navbar-brand" href="index.html">Maddy Ford</a>',
    'filename': 'content/blog_post.html',
    'output_filename': 'docs/blog_post.html',
    'active_class': 'post_active',
    },
    {
    'title': 'Contact',
    'headline': "Let's Get in Touch!",
    'brand': '<a class="navbar-brand" href="index.html">Maddy Ford</a>',
    'filename': 'content/contact.html',
    'output_filename': 'docs/contact.html',
    'active_class': 'contact_active',
    },
    {
    'title': 'Portfolio',
    'headline': 'My Work',
    'brand': '<a class="navbar-brand" href="index.html">Maddy Ford</a>',
    'filename': 'content/portfolio.html',
    'output_filename': 'docs/portfolio.html',
    'active_class': 'portfolio_active',
    }
]

blog_posts = [
    {
    'blog_post_title': 'Test1',
    'blog_post_text': 'blog_posts/1.html',
    'blog_post_output_filepath': 'docs/blog_post_1',
    'blog_post_date': 'May 26, 2018',
    },
    {
    'blog_post_title': 'Test2',
    'blog_post_text': 'blog_posts/2.html',
    'blog_post_output_filepath': 'docs/blog_post_2',
    'blog_post_date': 'May 27, 2018',
    },
    {
    'blog_post_title': 'Test3',
    'blog_post_text': 'blog_posts/3.html',
    'blog_post_output_filepath': 'docs/blog_post_3',
    'blog_post_date': 'May 28, 2018',
    },
]
# def templating():
    # for x in pages:
    #     template = open('templates/base.html').read()
    #     content = open(x['filename']).read()
    #     finished_content = content.replace('{{headline}}', x['headline'])
    #     replace('{{' + x['active_class'] + '}}', 'active')
    #     finished_page = template.replace('{{content}}', finished_content).replace('{{title}}', 'Maddy Ford - ' + x['title']).replace('{{brand}}', x['brand'])
    #     return finished_page

def main():
    for x in pages:
        template = open('templates/base.html').read()
        content = open(x['filename']).read()
        finished_content = content.replace('{{headline}}', x['headline'])
        finished_page = template.replace('{{content}}', finished_content).replace('{{title}}', 'Maddy Ford - ' + x['title']).replace('{{brand}}', x['brand']).replace('{{' + x['active_class'] + '}}', 'active')
        open(x['output_filename'], 'w+').write(finished_page)


#the below function is just for the landing page
def landing():
    template = open('templates/base-landing.html').read()
    content = open('content/index.html').read()
    finished_landing_page = template.replace('{{content}}', content).replace('{{title}}', 'Maddy Ford')
    open('docs/index.html', 'w+').write(finished_landing_page)

if __name__ == '__main__': #why is this function needed, and why is this the way it's being called? Because you don't want it being called anytime you run file
    main()
    landing()
# still in testing phase
# def blog():
#     for x in blog_posts:
#         #update blog page
#         blog_template = open('docs/blog.html').read()
#         finished_blog_page = blog_template.replace('{{blog_post_title}}', x['blog_post_title']).replace('{{blog_post_output_filepath}}', x['blog_post_output_filepath']).replace('{{blog_post_date}}', x['blog_post-date'])
#         open(x['blog_post_output_filepath'], 'w+').write(finished_blog_page)
#         #update individual blog post page
#         blog_post_template = open('docs/blog_post.html').read()
#         blog_content = open(x['blog_post_text']).read()
#         finished_blog_post = blog_post_template.replace('{{blog_post_title}}', x['blog_post_title']).replace('{{blog_post_date}}', x['blog_post-date']).replace('{{blog_post_text}}', x['blog_post_text'])
#         open(x['blog_post_output_filepath'], 'w+').write(finished_blog_post)
# if __name__ == '__blog__':
#     blog()
