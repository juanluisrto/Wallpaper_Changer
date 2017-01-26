import os,sys, re, urllib2, ctypes, random

directory = os.getcwd()
# You can alternatively choose another path to store the data by setting directory = "your\full\path" 
def main():
	if not os.path.exists(directory):
	    os.makedirs(directory)
	    os.makedirs(directory + "\images")
	    f = open(directory +"\data.txt",'w')   # Trying to create a new file or open one
	    f.close()
	import_data()
	search_wallpaper()
	set_wallpaper()

def import_data():
	global t_tags,f_tags,urls, number_of_downloads,img_resolution
	f = open(directory +"\data.txt")
	data = f.readlines()
	img_resolution= data[1][11:]
	t_tags = data[4].split(', ') #Thematic tags
	f_tags = data[7].split(', ') #Forbidden tags
	urls   = data[10:]
	number_of_downloads= len(urls)
	f.close()
	t_tags[-1] = t_tags[-1].replace('\n','')
	f_tags[-1] = f_tags[-1].replace('\n','')
	for i in range(len(urls)): urls[i]= urls[i].replace('\n','')


def search_wallpaper():
	random.shuffle(t_tags)
	success= False
	j = 0
	while success==False: 
		html_site = urllib2.urlopen('http://wallpaperswide.com/tag/'+ t_tags[j]).read()

		pagination=  re.findall(r'<a href="/tag/' + re.escape(t_tags[j]) + r'/page/(.*?)">',html_site) #returns list of numbers found
		try:
			page_number = random.randrange(int(max(pagination))) + 1   #selects randomly the page we are going to search on
		except:
			page_number=""
	  	html_site = urllib2.urlopen('http://wallpaperswide.com/tag/' + t_tags[j] + '/page/' + str(page_number)).read()
		aux= re.findall(r'align="center">\n        <a href="(.+.html)',html_site) #finds the links of all the found wallpapers in the page n with the chosen tag
		random.shuffle(aux) 
		links =[]
		for i in aux:
			links.append('http://wallpaperswide.com'+i) 
		for i in links:
			if check_if_used_before(i)==False and detect_valid_wallpaper(i)==True:
				download_wallpaper(i)
				f = open(directory +"\data.txt",'a')
				f.write(i + "\n")
				f.close()
				
				success=True
				break
		
		j = (j+1)%len(t_tags)
	


def check_if_used_before(link):
	for i in urls:
		if link == i: return True
	return False


def detect_valid_wallpaper(link):
	html_site = urllib2.urlopen(link).read()
	tags = re.findall(r'<a href="/tag/(\w{,}).html',html_site)
	for t in tags: 
		if t in f_tags: return False       #Checks if any tag is in the forbidden tags list
	return True

def download_wallpaper(link):
	html_site = urllib2.urlopen(link).read()
	download_link = "http://wallpaperswide.com/download/" + link[26:-6] +"-" + str(img_resolution)[:-1] + ".jpg"
	  
	values = {'Accept':"image/webp",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Connection":"keep-alive",
	"Referer": link,
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":""
	 }
	req = urllib2.Request(download_link, headers=values)
	response=urllib2.urlopen(req)
	img = response.read()
	image = open(directory + "\images\wallpaper_" + "%d.jpg"%number_of_downloads ,'wb')
	image.write(img)
	image.close()




def set_wallpaper():
	img = directory + '\images\wallpaper_' + str(number_of_downloads) + '.jpg'
	ctypes.windll.user32.SystemParametersInfoA(20, 0, img , 0)
	#if you are not using Windows, you should search for the function which changes the wallpaper in your OS




main()
	 
