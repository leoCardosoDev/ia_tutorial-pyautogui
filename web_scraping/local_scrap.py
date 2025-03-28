from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    content = file.read()

ex = BeautifulSoup(content, "lxml")
# print(ex.prettify())
print(ex.title)
print(ex.find("p"))
print(ex.find_all("p"))
print(ex.find_all("p")[0])
print(ex.find_all("p")[0].text)

print('--__--' * 20)
print(ex.find_all(class_="title"))

tags = ex.find_all(class_="title")
for tag in tags:
    print(tag)