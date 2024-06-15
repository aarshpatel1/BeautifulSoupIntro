from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tags = soup.select(".title a")
print(article_tags)

# article_text = article_tags.getText()
# print(article_text)

article_texts = [text.getText() for text in article_tags]
print(article_texts)

# article_link = article_tags.get("href")
# print(article_link)

article_links = [link.get("href") for link in article_tags]
print(article_links)

article_upvotes = [int(upvote.getText().split(" ")[0]) for upvote in soup.find_all(name="span", class_="score")]
print(article_upvotes)

max_upvote = max(article_upvotes)
print(max_upvote)
max_upvote_index = article_upvotes.index(max_upvote)
print(max_upvote_index)

print(article_texts[max_upvote_index])
print(article_links[max_upvote_index])
print(article_upvotes[max_upvote_index])
