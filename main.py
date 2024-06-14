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
# print(
#     soup.find("h1"))  # returns the first h1 tag [NOTE: It can be any tag but find returns the first one that matches)

# print(soup.p)  # returns the first p (paragraph) tag of the website
# print(soup.a)  # returns the first a (anchor) tag of the website
# print(soup.li)  # returns the first li (list) tag of the website

# all_anchor_tags = soup.find_all(name="a")  # returns all the anchor tags inside the html code as a list
# print(all_anchor_tags)

# returns the text content between anchor tags using list comprehension
# all_anchor_tag_content = [content.string for content in all_anchor_tags]  # method 1
# all_anchor_tag_content = [content.getText() for content in all_anchor_tags]  # method 2
# print(all_anchor_tag_content)

# returns the links in href attribute of anchor tags using list comprehension
# all_anchor_tag_href_links = [link.get("href") for link in all_anchor_tags]
# print(all_anchor_tag_href_links)

# returns the particular html element that has given parameters (here) like tag's name and tag's id
# heading = soup.find(name="h1", id="name")
# print(heading)

# returns the first h3 (here) tag that has class name "heading"
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# returns the classes of the html element as a list
print(section_heading.get("class"))

# NOTE: "class" is a reserved keyword in python so that we cannot give our argument name "class".
#       That's why here we will use "class_" as a name of the attribute defined in the bs4 package module

# returns all h3 tags that have class name "heading" as a list even if there is only one
all_section_heading = soup.find_all(name="h3", class_="heading")
print(all_section_heading)

# returns the particular html element using css selectors,
# and it will return the first element that matches the selector path
# company_url = soup.select_one(selector="p a")
# print(company_url)

# returns all the html element that matches given css selector as a list even if it is only one
company_url = soup.select(selector="p a")
print(company_url)

# returns the html element by given css id selector
name = soup.select_one(selector="#name")
print(name)
print(name.string)

# return all the html element by given css class selector as a list
section_headings = soup.select(".heading")
print(section_headings)
