#!/usr/bin/env python
from common import base

def get_title():
    page_title = raw_input('Enter page title:')
    return page_title

def get_page_contents():
    done = False
    content = ''
    title = raw_input("Enter Title: ")
    content = '<center><h2>{0}</h2></center>'.format(title)

    while not done:
        content_type = raw_input("Select input content (T) for plain test, "
                             "(L) for list 'Dv' for div 'D' for Done: ")
        if content_type.lower() == 'l':
            my_list = create_list()
            content += '\n' + my_list
        if content_type.lower() == 't':
            text = create_text_content()
            content += '\n' + text
        if content_type.lower() == 'dv':
            div_text = create_div_content()
            content += div_text
        if content_type.lower() == 'd':
            done = True
    return content

def create_list():
    list_type = '<ul>{0}</ul>'
    order = raw_input('Order list (Y/N): ')
    if order.lower() == 'y':
        list_type = '<ol>{0}</ol>'
    items = ''

    more_item = True
    while more_item:
        str_item = raw_input("Enter line item: ")
        has_link = raw_input("Has link (Y/N): ")
        if has_link.lower() == 'y':
            get_link = create_link()
            str_item += get_link
        more_text = raw_input("More text (Y/N): ")
        if more_text.lower() == 'y':
            get_text = create_text_content()
            str_item += get_text
        list_item = ('<li>{0}</li>').format(str_item)
        items += list_item
        more = raw_input("More entries (Y/N):")
        if more.lower() == 'n':
            more_item = False
    my_list = list_type.format(items)
    return my_list

def create_text_content():
    text = ''
    more_text = True
    while more_text:
        get_text = raw_input("Enter content: ")
        text += get_text
        text += '\n'
        has_link = raw_input("Has link (Y/N): ")
        if has_link.lower() == 'y':
            get_link = create_link()
            text += get_link
        more = raw_input("More text (Y/N): ")
        if more.lower() == 'n':
            more_text = False
    return text

def create_div_content():
    div_tag = '<div>{0}</div>'
    more = True
    div_content = ''
    while more:
        get_content = raw_input("Enter content: ")
        div_content += get_content
        has_link = raw_input("Has link (Y/N): ")
        if has_link.lower() == 'y':
            get_link = create_link()
            div_content += get_link
        more = raw_input("More text (Y/N): ")
        if more.lower() == 'n':
            more = False
        div_tag = div_tag.format(div_content)
    return div_tag

def create_link():
    link_tag = '<a href="{link}" {js_option}>{link_text}</a>'
    more = True
    get_link = raw_input("Enter link: ")
    get_link_name = raw_input("Link text: ")
    have_js = raw_input("Have javascript (Y/N): ")
    js_content = ''
    if have_js.lower() == 'y':
        js_content = 'onclick="{0}"'
        content = raw_input("Enter javascript content: ")
        js_content.format(content)

    link_tag = link_tag.format(link=get_link, js_option=js_content,
                               link_text=get_link_name)
    return link_tag

def build_html_doc(title=None, body=None):
    if not title:
        title = 'JV doc'
    if not body:
        body = 'Should start with something...'
    html_doc = ('<html><header><title>{'
                'site_title}</title></header><body>{'
                'body}</body></body></html').format(site_title=title,
                                                    body=body)
    return html_doc

def generate_html_file(file_name=None, html_doc=None):
    home_dir = base.get_base_dir()
    if not file_name:
        file_name = home_dir + '/test.html'
    if not html_doc:
        html_doc = ('<html><header><title>jv '
                    'doc</title></header><body>Start with '
                    'something...</body></html>')
    my_html_file = open(file_name, 'w')
    my_html_file.write(html_doc)

if __name__ == '__main__':
    title = get_title()
    contents = get_page_contents()
    html_doc = build_html_doc(title=title, body=contents)
    file_name = raw_input("Save as file name: ")
    if '.html' not in file_name or '.htm' not in file_name:
        file_name += '.html'
    generate_html_file(file_name=file_name, html_doc=html_doc)
