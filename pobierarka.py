from pytube import *
from time import *
import urllib.request
import re

#download single vid
def pobier(lunk):
	if 'youtube' not in lunk:
		lunk = 'https://www.youtube.com/watch?v='+lunk
	try:
		vid=YouTube(lunk, on_progress_callback=progress_check)
		print("I download for U:",vid.title)
		strim=vid.streams.get_highest_resolution().download()
		print("100.00%")
	except Exception as e:
		print("Somethin went horribly rong :<")
		print(e)

#download playlist		
def pobier_liste(link_listy, ile=1000):
	x = urllib.request.urlopen(link_listy).read()
	x = set(re.findall(r'"videoId":"([^"]*)"',x.decode("utf-8")))
	all_vid=len(x)
	pobrane=[]
	for vid,i in enumerate(x):
		print(str(i+1)+"/"+str(all_vid),end=" ")
		if vid in pobrane:
			continue
		if i<ile: 
			pobier(vid)
			pobrane.append(vid)
		else: 
			break

#progress percentage visualization
def progress_check(stream = None, chunk = None, file_handle = None, remaining = None):
	all+=len(chunk)
	elapsed_time+=time()-now
	now=time()
	percent=all/stream.filesize*100
	remaining_time=(elapsed_time*100/percent)*((100-percent)/100)
	hours=int(remaining_time/3600)
	minutes=int((remaining_time-hours*3600)/60)
	seconds=int(remaining_time-hours*3600-minutes*60)
	print("{:.2f}% passed {}s, ETA app. {}h {}min {}s         ".format(percent,int(elapsed_time),hours,minutes,seconds), end='\r')