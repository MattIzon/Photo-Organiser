import os
import re
from datetime import datetime

PATH = "/home/matt/Desktop/Camera" # insert filepath here

months = {"01":"January", "02":"February",
		  "03":"March", "04":"April",
		  "05":"May", "06":"June",
		  "07":"July", "08":"August",
		  "09":"September", "10":"October",
		  "11":"November", "12":"December"}

class Expression(object):
	"""Contain filename meta-data in a single structure."""
	def __init__(self, regex, year_start, year_end, month_start, month_end, timestamp=False):
		self.style = regex
		self.year = slice(year_start, year_end)
		self.month = slice(month_start, month_end)
		self.timestamp = timestamp

expressions = {
"Camera": Expression(re.compile("\d{8}(_|-)\d{6}((_|-)\d*)?(\(\d*\))?\.((jpe?g)|(mp4)|(gif))"), 0, 4, 4, 6),
"WhatsApp": Expression(re.compile("((IMG)|(VID))(_|-)\d{8}(_|-)(WA)?\d{4,6}\.((jpe?g)|(mp4))"), 4, 8, 8, 10),
"Screenshot1": Expression(re.compile("Screenshot_\d{4}(-\d{2}){5}\.png"), 11, 15, 16, 18),
"Screenshot2": Expression(re.compile("Screenshot_\d{8}(_|-)\d{6}\.png"), 11, 15, 15, 17),
"Facebook": Expression(re.compile("(received)|(IMG)_\d*\.jpe?g"), 0, 4, 5, 7, True),}

for root, dirs, files in os.walk(PATH):
	for photo in files:
		for exp in expressions.values():
			if exp.style.match(photo):
				if exp.timestamp:
					time_data = str(datetime.fromtimestamp(os.stat("{0}/{1}".format(root, photo)).st_mtime))
				else:
					time_data = photo
				year = time_data[exp.year]
				month = time_data[exp.month]
				src = "{0}/{1}".format(root, photo)
				dest = "{0}/{1}/{2}_{3}/{4}".format(PATH, year, month, months[month], photo)
				os.renames(src, dest)
				break
