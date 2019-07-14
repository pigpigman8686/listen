import random
import os,re

def getMessage(yes=True,snr=28,count=1):
    if count == 1:
        page = int(9)
    elif yes==True:
        page = int((snr-10)/2-1)
        if page<0:
            page = 0
    else:
        page = int((snr-10)/2+1)
        if page>18:
            page=18
    filepath = "static/voice/"+str(page)
    #print("filepath:"+filepath)
    filelist = os.listdir(filepath) 
    #print("mess len:"+str(random.randint(0,len(message))))
    #print(random.randint(0,len(message)))
    message = "voice/"+str(page)+"/"+ str(filelist[random.randint(0,len(filelist)-1)])
    return message

def average(result):
    patten = re.compile('(\d{1,})-(\d{1,})')
    snr = 0
    for i in range(1,20):
        #print("--------------------i:"+str(i))
        s = '%s'%str(result[0]['right'+str(i)])
        right = re.search(patten,s)
        snr += int(right.group(2))
    return snr/19.0