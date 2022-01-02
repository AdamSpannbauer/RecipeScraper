from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/RuneScape"

# Pull down web page and extract html as text
response = requests.get(url)
html = response.text

# Run html through parser to interact with
parsed_html = BeautifulSoup(html, features="html.parser")

# h1, h2, h3 are the html tags for 1st, 2nd, 3rd level headers
header_tags = ["h1", "h2", "h3"]

# Find all of the above html tags in parsed html
headers_html = parsed_html.find_all(header_tags)

# Iterate over found headers, extract text, remove whitespace with strip()
headers_text = [h.text.strip() for h in headers_html]

print(headers_text)
# ['RuneScape', 'Contents', 'Gameplay', 'Skills', 'Combat', 'Non-player interaction',
#  'Player interaction', 'Quests', 'Development', 'Graphics and audio', 'Servers',
#  'Old School RuneScape', 'DarkScape', 'Community', 'Rules and cheating', 'Reception',
#  'Revenue', 'References', 'External links', 'Navigation menu', 'Personal tools',
#  'Namespaces', 'Variants\nexpanded\ncollapsed', 'Views', 'More\nexpanded\ncollapsed',
#  'Search', 'Navigation', 'Contribute', 'Tools', 'Print/export', 'In other projects', 'Languages']
