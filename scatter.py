

workdir="/media/linux/WORKDIR"


import os
path = os.path.join(workdir, "data.csv")

import pyautogui
import time
def csv_4scatter_w(x,y):	
	exists = None if not os.path.exists(path) else 1.
	
	with open (path, mode="a+") as data:
		data.seek(1)
		
		if not exists:
			data.write("x,y\n")

		else:
			
			position= "%s,%s\n" % (x,y)
			last_index = position != data.readlines() [-1]
			
			if last_index: 
				data.write(position)
				print(position.strip())
			
			
while 1.:
	
	x, y = pyautogui.position()
	# mouse imlecinin ekrandaki konumu
	
	csv_4scatter_w(x,y)
	time.sleep(.3)
