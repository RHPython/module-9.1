def urlify(string):
    strip_string=string.strip()
    title_case = string.title()
    url = title_case.replace(' ','_')
    return url

print(urlify('Rakib Hasan'))

