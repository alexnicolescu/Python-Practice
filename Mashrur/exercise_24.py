import requests
from bs4 import BeautifulSoup
from re import sub, compile

def remove_html_tags(text):
    clean = compile('<.*?>')
    return sub(clean, '', text)


url = 'http://www.nytimes.com/'
req = requests.get(url)
req_html = req.text
soup = BeautifulSoup(req_html)
stories_list = soup.find_all(class_="css-1vvhd4r e1voiwgp0")
file_name = str(input("Enter the name of the file where the text will be saved > "))
with open(file_name,"w") as f:
    for story_heading in stories_list:
        if story_heading.a:
            f.write(remove_html_tags(str(story_heading.a)))
        else:
            f.write(remove_html_tags(str(story_heading.contents[0])))
