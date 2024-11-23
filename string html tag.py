# def heading_two(text):
#     """
#     return heading two text of html
#     :param text : Any kind of string
#     :return : html tag
#     """
#     html = f'<h2>{text}</h2>'
#     return html

# print(heading_two.__doc__)


# def html_tag(text,html_tag):
#     """"
#     Return HTML Tag of any text
#     :param text : Any kind of string
#     :param html_tag:What kind of tag you want to generate
#     :return : HTML Tag of any text
#     """
#     html = f'<{html_tag}>{text}</{html_tag}>'
#
#
# print(html_tag('This is Paragraph','h6'))
def html_tag(text, html_tag):
    """
    Return HTML Tag of any text
    :param text: Any kind of string
    :param html_tag: What kind of tag you want to generate
    :return: HTML Tag of any text
    """
    html = f'<{html_tag}>{text}</{html_tag}>'
    return html  # Added return statement


print(html_tag('This is Paragraph', 'strong'))


