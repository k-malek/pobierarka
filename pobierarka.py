from pytube import *
from time import *
import urllib.request
import re

class Timer:
	def __init__(self,remaining):
		self.remaining=0
	def __enter__(self):
		self.start=time.now()
		return self
	
def pobier(lunk):
	try:
		global all
		global elapsed_time
		global now
		all=0
		elapsed_time=0
		now=time()
		vid=YouTube('https://www.youtube.com/watch?v='+lunk, on_progress_callback=progress_Check)
		print("Oto pobieram Ci:",vid.title)
		strim=vid.streams.get_highest_resolution()
		strim.download()
		print("100.00%")
	except Exception as e:
		print("Nie pykuo :<")
		print(e)
		
def pobier_liste(link_listy, ile=1000):
	x = urllib.request.urlopen(link_listy)
	x = x.read()
	x = re.findall(r'"videoId":"([^"]*)"',x.decode("utf-8"))
	x = set(x)
	i=0
	all_vid=len(x)
	pobrane=[]
	for vid in x:
		print(str(i+1)+"/"+str(all_vid),end=" ")
		if vid in pobrane:
			continue
		if i<ile: 
			pobier(vid)
			pobrane.append(vid)
		else: 
			break
		i+=1
		
def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
	global all
	global elapsed_time
	global now
	all+=len(chunk)
	elapsed_time+=time()-now
	now=time()
	percent=all/stream.filesize*100
	remaining_time=(elapsed_time*100/percent)*((100-percent)/100)
	hours=int(remaining_time/3600)
	minutes=int((remaining_time-hours*3600)/60)
	seconds=int(remaining_time-hours*3600-minutes*60)
	print("{:.2f}% upłynęło {}s pozostało ok. {}h {}min {}s         ".format(percent,int(elapsed_time),hours,minutes,seconds), end='\r')
	