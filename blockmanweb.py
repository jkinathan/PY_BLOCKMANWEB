#mac and linux /etc/hosts
#windows: c:\Windows\System32\drivers\etc\hosts
#bt u need to run this program during bootup of the system
#by adding blockmanweb.py in the cron table because i am using linux mint
#this is done by opening cron using command "sudo crontab -e" then add ..
#this to the end of the line "@reboot python3 /home/kinathan/Desktop/blockmanweb.py" this is the hosts_path
#to your python application to run at the start
import time
from datetime import datetime as dt #importing dattime and using sgort form as dt
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.youtube.com"]
hosts_temp = "hosts"
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Your working HOURS...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"   "+website+"\n")

    else:
        with open(hosts_path,'r+') as file:# open host file in read and append
            content = file.readlines()#this stores lines in content
            #file.seek(0) ....this takes the pointer to the firstplace of the file hosts
            for line in content:
                if not any(website in line for website in website_list):
                #if any of the websites is not in the current line of the content list then we write down that line in the host file
                    file.write(line)
            #for.truncate() ...thisremoves all lines after the pointer position
            #then we truncate all the lines after the contents
        print("Fun Hours...ENJOY!")
    time.sleep(5)
