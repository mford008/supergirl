import glob
import os
from jinja2 import Template
import markdown

blog_posts = []
pages = []
landing = {
    'base': 'templates/base-landing.html',
    'page': 'landing/index.md',
    'title': 'Maddy Ford'
}

def main():
    #writing all main pages (not individual blog posts)
    all_content_files = glob.glob('content/*.md')
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
            files = pages
        )
        open(page['output_filepath'], 'w+').write(finished_page)

def append(file_name, name_only):
    #appending keys to pages list
    pages.append({
        'filepath': 'content/'+str(file_name),
        'filename': file_name,
        'name': name_only,
        'output_filepath': 'docs/'+str(name_only) + '.html',
        'output_filename': str(name_only) + '.html',
        'title': 'Maddy Ford - ' + name_only,
    })

def blog_append(file_name, name_only):
    #appending keys to blog_posts list
    blog_posts.append({
        'filepath': 'blog_posts/'+str(file_name),
        'filename': file_name,
        'name': name_only,
        'output_filepath': 'docs/'+str(name_only) + '.html',
        'output_filename': str(name_only) + '.html',
        # 'title': post_title,
    })

def convert(page):
    #markdown conversion for all pages but landing
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    md_content = open(page).read()
    html = md.convert(md_content)
    return html

def convert_landing(landing_content_file):
    #markdown conversion for landing
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    md_content = open('landing/index.md').read()
    html = md.convert(md_content)
    return html


def landing():
    #creating docs landing page
    landing_content_file = glob.glob('landing/*.md')
    for page in landing_content_file:
        convert_landing(landing_content_file)
        template_html_landing = open('templates/base-landing.html').read()
        content = open('landing/index.md').read()
        template = Template(template_html_landing)
        finished_landing_page = template.render(
            title = "Maddy Ford",
            content = content,
        )
    open('docs/index.html', 'w+').write(finished_landing_page)

landing()

def compile_blog_posts():
    all_blog_posts = glob.glob('blog_posts/*.md')
    for page in all_blog_posts:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        convert(page)
        blog_append(file_name, name_only)
    for page in blog_posts:
        content_html_post = open(page['filepath']).read()
        template_html_post = open('templates/base-blog-posts.html').read()
        template_post = Template(template_html_post)
        finished_blog_post = template_post.render(
            title = name_only,
            content = content_html_post,
        )
        open(page['output_filepath'], 'w+').write(finished_blog_post)
    for page in blog_posts:
        template_html_main = open('templates/base-blog.html').read()
        template_main = Template(template_html_main)
        finished_blog_page = template_main.render(
            title = name_only,
            filepath = page['filepath'],
            blog_posts = blog_posts,
        )
    print(blog_posts)
    open('docs/blog.html', 'w+').write(finished_blog_post)

compile_blog_posts()

if __name__ == '__main__':
    main()
