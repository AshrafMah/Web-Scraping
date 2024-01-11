import requests  # allow you to download the HTML
from bs4 import BeautifulSoup  # allow you to use HTML and grap different data
import pprint

def get_hn_page(n):
    url = f'https://news.ycombinator.com/?p={n}'
    res = requests.get(url)
    return res

def scrape_multiple_pages(pages):
    all_hn = []
    for page_number in range(1, pages + 1):
        res = get_hn_page(page_number)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline > a')
        subtext = soup.select(".subtext")
        results = create_custom_hn(links, subtext)
        all_hn.extend(results)
    return all_hn

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

# Specify the number of pages to scrape
number_of_pages = 5

# Scrape multiple pages
results = scrape_multiple_pages(number_of_pages)

# Print the results
pprint.pprint(results)
