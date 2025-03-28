from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    content = file.read()

ex = BeautifulSoup(content, "lxml")
print(ex.prettify())
