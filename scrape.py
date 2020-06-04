import requests 
from bs4 import BeautifulSoup 
import json
insta_url = 'https://instagram.com'
def get_account_info(profile_username: str):
	response = requests.get(f"{insta_url}/{profile_username}")
	if response.ok:
		soup = BeautifulSoup(response.text, 'lxml')
		scripts = soup.select('script[type="application/ld+json"]')
		scripts_content = json.loads(scripts[0].text.strip())
		content_info = ["@type", "name", "description", "url"]	
		for each_word in content_info:
			try:
	
				print(scripts_content[f'{each_word}'])

			except:
				pass
get_account_info('pornhub')
