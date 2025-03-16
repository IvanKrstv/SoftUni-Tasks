import re

pattern_title = r'<title>(.*?)<\/title>'
patter_body = r'<body>(.*?)<\/body>'

html = input()
title = re.search(pattern_title, html).group(1)
content = re.search(patter_body, html).group(1)

clean_content = re.sub(r'<.*?>', '', content)
cleaner_content = re.sub(r'\\n', '', clean_content)

print(f"Title: {title}\nContent: {cleaner_content}")

#<html>\n<head><title>Some title</title></head>\n<body>Here<p> is some </p>content <a href="www.somesite.com">\nclick</body>\n</html>