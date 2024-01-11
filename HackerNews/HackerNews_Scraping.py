import requests  # allow you to download the HTML
from bs4 import BeautifulSoup  # allow you to use HTML and grap different data
import pprint

res = requests.get('https://news.ycombinator.com/news')

# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')  # converted to HTML format
links = soup.select('.titleline > a')
subtext = soup.select(".subtext")
# print(links[0])
# print(votes[0])

def sort_stories_by_votes(hnList):
    return sorted(hnList, key = lambda k:k['votes'], reverse=True)



def create_custom_hn(links, subtext):
    hn = []  # Initialize an empty list to store the extracted information

    for idx, item in enumerate(links):
        title = item.getText()  # Extract the text content of the link at the current index
        href = item.get('href', None)  # Extract the 'href' attribute of the link at the current index
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))  # Extract and convert the points to an integer
            if points > 99:
                hn.append({'title':title, 'link':href, 'votes':points})  # Append a dictionary with extracted information

    return sort_stories_by_votes(hn) # Return the list of dictionaries containing extracted information

pprint.pprint(create_custom_hn(links, subtext))
