from pytube import *
from time import *
import urllib.request, re, math, os

#download single vid
def pobier(lunk,path=''):
    global all
    global elapsed_time
    global now
    all=0
    elapsed_time=0
    now=time()
    if 'youtube' not in lunk:
        lunk = 'https://www.youtube.com/watch?v='+lunk
    try:
        vid=YouTube(lunk, on_progress_callback=progress_check)
        print("I download for U:",vid.title)
        if(path==''):
            strim=vid.streams.get_highest_resolution().download()
        else:
            strim=vid.streams.get_highest_resolution().download(path)
        print("100.00%")
    except Exception as e:
        print("Somethin went horribly rong :<")
        print(e)

#download playlist        
def pobier_liste(link_listy, ile=1000):
    x = urllib.request.urlopen(link_listy).read()
    x = re.findall(r'"videoId":"([^"]*)"',x.decode("utf-8"))
    all_vid=len(x)
    pobrane=[]
    for i,vid in enumerate(x):
        print(str(i+1)+"/"+str(all_vid),end=" ")
        if vid in pobrane:
            continue
        if i<int(ile): 
            pobier(vid)
            pobrane.append(vid)
        else: 
            break

#download videos from channel            
def pobier_kanal(channel_name,ile=5):
    curr_path=os.getcwd()
    path=curr_path+r"/"+channel_name
    if not os.path.exists(path):
        os.mkdir(path)
    c=Channel('https://www.youtube.com/c/'+channel_name)
    i=0
    for vid in c.video_urls:
        print(str(i+1)+r"/"+str(min(ile,len(c.video_urls))))
        pobier(vid,path)
        i+=1
        if i==ile or i==len(c.video_urls):
            break
            
#progress percentage visualization
def progress_check(stream = None, chunk = None, file_handle = None, remaining = None):
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
    strokes_for_bar=math.floor(percent//5)
    print("{:.2f}% [".format(percent)+"="*strokes_for_bar+"-"*(20-strokes_for_bar)+"] passed {}s, ETA app. {}h {}min {}s         ".format(int(elapsed_time),hours,minutes,seconds), end='\r')