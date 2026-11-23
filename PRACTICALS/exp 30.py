title = input("Enter Blog Title: ")
content = input("Enter Blog Content: ")
link = input("Enter Website Link: ")

html = f"""
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{content}</p>
    <a href="{link}">Visit Website</a>
</body>
</html>
"""

with open("blog.html", "w") as file:
    file.write(html)

print("Blog Created Successfully!")
