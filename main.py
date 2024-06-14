from bs4 import BeautifulSoup

with open("website.html") as website:
    contents = website.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")

# print(soup)  # returns all the html code
# print(soup.prettify())  # returns the all html code with proper indentation
# print(soup.title)  # returns the title tag
# print(soup.title.name)  # returns the name of the tag (here it is title tag)
# print(soup.title.string)  # returns the content inside the title tag
#
# print(soup.p)  # returns the first p (paragraph) tag of the website
# print(soup.a)  # returns the first a (anchor) tag of the website
# print(soup.li)  # returns the first li (list) tag of the website
