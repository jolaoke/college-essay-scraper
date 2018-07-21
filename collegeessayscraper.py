
import urllib3
import re
from bs4 import BeautifulSoup as bs

http = urllib3.PoolManager()
url = "https://www.collegevine.com/college-essay-prompts/"
response = http.request('GET', url)
soup = bs(response.data)

run = True
while run:
	print("Enter 'list' below to view a complete list of colleges with supplemental essays.")
	print("Enter 'quit' to exit.")
	college = input("Enter the full name of a college/university: ")
	college = college.lower().replace(" ", "-")

	if college == "list" or college == "List":
		all_colleges = soup.find_all('a', href=re.compile("accordion"))
		for college in all_colleges:
			print(college.text)

	elif college == "quit" or college == "Quit":
		run = False
		break

	else:
		try:
			all_prompts = soup.find('div', id=college).find('div', id=re.compile("accordion")).find_all('div', class_="prompt-wrapper")
			list_of_prompts = []
			for prompt in all_prompts:
				list_of_prompts.append(prompt.text.replace("                         ", "").replace("                      ",""))

			print("Number of essays: " + str(len(list_of_prompts)) + "\n")
			n = 1
			for prompt in list_of_prompts:
				print("Essay " + str(n) + ":")
				print(prompt)
				n += 1
		except AttributeError:
			print("The college/university you entered either has no supplemental essay or was misspelled.")