import requests
import urllib2
import os
import boto
import callme
from twilio.rest import TwilioRestClient
from random import randint

done = False

def upload():
	s3 = boto.connect_s3()
	bucket = s3.create_bucket('twitchioz')
	key = bucket.new_key('dataud.mp3')
	key.set_contents_from_filename('/home/taemin/Twitchioz/audio.mp3')
	key.set_acl('public-read')
	return "https://s3.amazonaws.com/twitchioz/dataud.mp3"	

def getVidId(streamer):
	channel = "https://api.twitch.tv/kraken/channels/"+streamer+"/videos?limit=10&broadcasts=true"
	r = requests.get(channel).json()

	#idnum = r['videos'][2]['_id']
	idnum = r['videos'][randint(0,8)]['_id']
	idnumbz = idnum[1:len(idnum)]
	
	return idnumbz

def getVidFile(idnumb):
	url = "http://api.justin.tv/api/broadcast/by_archive/"+str(idnumb)+".json"
	r = requests.get(url).json()
	
	gurl = r[0]['video_file_url']	

	file_name = gurl.split('/')[-1]
	u = urllib2.urlopen(gurl)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)
	
	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	f.close()
	return file_name

def vid2mp3(vidfile):
	cmnd = "ffmpeg -i " + vidfile + " -ab 160k -ac 2 -ar 44100 -vn audio.mp3"
	os.system(cmnd)
	retStr = upload()
	done = True
	return retStr

def main():
		
	streamer = raw_input("Enter the channel you want to check out: ")
	vid2mp3(getVidFile(getVidId(streamer)))	
	callme.call()
	#vid2mp3("live_user_day9tv_1381197419.flv")
	
	
if __name__ == '__main__':
	main()	
