title_article = input()
print(f"<h1>"
      f"\n\t{title_article}"
      f"\n</h1>")

content_article = input()
print(f"<article>"
      f"\n\t{content_article}"
      f"\n</article>")

while True:
    comment = input()
    if comment == "end of comments":
        break

    print(f"<div>"
          f"\n\t{comment}"
          f"\n</div>")