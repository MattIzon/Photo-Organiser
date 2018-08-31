import os
import re
from datetime import datetime

PATH = "/home/matt/Desktop/s62018" # insert filepath here

months = {"01":"January", "02":"February",
		  "03":"March", "04":"April",
		  "05":"May", "06":"June",
		  "07":"July", "08":"August",
		  "09":"September", "10":"October",
		  "11":"November", "12":"December"}

# split expressions in to single expressions
# name them better
# put into a dictionary
Camera = re.compile("\d{8}(_|-)\d{6}((_|-)\d*)?(\(\d*\))?\.((jpe?g)|(mp4)|(gif))")
WhatsApp = re.compile("((IMG)|(VID))(_|-)\d{8}(_|-)(WA)?\d{4,6}\.((jpe?g)|(mp4))")
Screenshot1 = re.compile("Screenshot_\d{4}(-\d{2}){5}\.png")
Screenshot2 = re.compile("Screenshot_\d{8}(_|-)\d{6}\.png")
Facebook = re.compile("(received)|(IMG)_\d*\.jpe?g")

#Screenshot_20170915-160632.png

for root, dirs, files in os.walk(PATH):
	for photo in files:
		if Camera.match(photo):
			year = photo[0:4]
			month = photo[4:6]
		elif WhatsApp.match(photo):
			year = photo[4:8]
			month = photo[8:10]
		elif Screenshot1.match(photo):
			year = photo[11:15]
			month = photo[16:18]
		elif Screenshot2.match(photo):
			year = photo[11:15]
			month = photo[15:17]
		elif Facebook.match(photo):
			timestamp = str(datetime.fromtimestamp(os.stat(root + "/" + photo).st_mtime))
			year = timestamp[0:4]
			month = timestamp[5:7]
		else:
			continue
		src = root + "/" + photo
		dest = PATH + "/" + year + "/" + month + "_" + months[month] + "/" + photo
		os.renames(src,dest)
