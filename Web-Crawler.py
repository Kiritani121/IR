import requests
from bs4 import BeautifulSoup

def get_links(url):
    # Retrieve the HTML content of the URL
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract all the links from the page
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href is not None and href.startswith("http"):
            links.append(href)

    return links

# Example usage
links = get_links("https://ruiacollege.edu/Default.aspx")

for link in links:
    print(link)
