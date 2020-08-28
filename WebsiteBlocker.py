while input('hello,would u like repetition?(y/n)')=='y':
	input()
	guesi()

from datetime import datetime
host='C:\\Windows\\System32\\drivers\\etc\\hosts'
redirect='127.0.0.1'

websites=['facebook.com','www.facebook.com','www.instagram.com']
start=datetime(2020,8,14)
end=datetime(2020,8,15)
todayt=datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
	if start<=todayt<end:
		with open(host,'r+') as file:
			content=file.read()
			for site in websites:
				if site in content:
					pass
				else:
					file.write(redirect+" "+site+"\n")
		print('al sites blocked')
		break
	else:
		with open(host,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(site in line for site in websites):
					file.write(line)
			file.truncate()
		print('all sites unblocked')
		break
import  random