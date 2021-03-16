from bs4 import BeautifulSoup
import requests
import lxml
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
csv_file = open('cms_scrape.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

#print(soup.prettify())

for article in soup.find_all('article'):
#print(article.prettify())

	headline = article.h2.a.text
	print(headline)
	print()

	summary = article.find('div', class_='entry-content').p.text
	print(summary)
	print()

	vid_dict = article.find('iframe', class_='youtube-player')
#	if vid_dict != None:
#		vid_src = vid_dict['src']
#		#vid_src = article.find('iframe', class_='youtube-player')['src']
#		#print(vid_src)

#		vid_id = vid_src.split('/')[4]
#		vid_id = vid_id.split('?')[0]
		#print(vid_id)

#		yt_link = f'https://youtube.com/watch?v={vid_id}'
		#yt_link2 = 'https://youtube.com/watch?v=' + vid_id
#		print(yt_link)
		#print(yt_link2)
#	else:
#		print(' --- no youtube video link attached ---')
		
	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']
		#print(vid_src)
		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]
		#print(vid_id)
		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = '--- no youtube video link attached ---'
	
	print(yt_link)	
	print()
	
	#not working ???
	csv_writer.writerow([headline, summary, yt_link])
	#csv_writer.writerow([headline.encode('utf-8'), 'summary', 'yt_link'])

csv_file.close()




