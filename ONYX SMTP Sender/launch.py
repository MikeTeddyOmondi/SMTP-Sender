import os
from colorama import Fore, init
import os
from os import system
from colorama import Fore, init
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
os.system('mode con cols=150 lines=35')
class colors:
    red = "\033[31m"
    yellow = "\33[33m"
    green = "\33[92m"
    purple = "\033[35m"
    reset = "\33[37m"

menu="""
              



           ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗    ███████╗███╗   ███╗████████╗██████╗     ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
          ██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝    ██╔════╝████╗ ████║╚══██╔══╝██╔══██╗    ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
          ██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝     ███████╗██╔████╔██║   ██║   ██████╔╝    ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
          ██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗     ╚════██║██║╚██╔╝██║   ██║   ██╔═══╝     ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
          ╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗    ███████║██║ ╚═╝ ██║   ██║   ██║         ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
           ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝         ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                  



""".replace("█", Fore.RED+"█"+Fore.RESET)
pub = colors.red+"                           ["+colors.reset+"   Dev by Esio#4847  "+colors.red+"|"+colors.reset+"  Github.com/Esio-01  "+colors.red+"|"+colors.reset+"  discord.gg/onyxfr  "+colors.red+"|"+colors.reset+"  Telegram: t.me/onyxfr   "+colors.red+"]"
print(menu)
print(pub)
print()
print()
print()
print(colors.red+"            ╔═["+colors.reset+"smtp server"+colors.red+"]")
server=input("            ╚══● "+colors.green)
print()
print(colors.red+"            ╔═["+colors.reset+"server port"+colors.red+"]")
port=input("            ╚══● "+colors.green)
print()
print(colors.red+"            ╔═["+colors.reset+"sender's email"+colors.red+"]")
sender=input("            ╚══● "+colors.green)
print()
print(colors.red+"            ╔═["+colors.reset+"email ID"+colors.red+"]")
id=input("            ╚══● "+colors.green)
print()
print(colors.red+"            ╔═["+colors.reset+"email password"+colors.red+"]")
password=input("            ╚══● "+colors.green)
print()
print(colors.red+"            ╔═["+colors.reset+"email list file(.txt)"+colors.red+"]")
list=input("            ╚══● "+colors.green)
print()
print(colors.red+"            ╔═["+colors.reset+"subject"+colors.red+"]")
subject=input("            ╚══● "+colors.green)
print()
print(colors.red+"            ╔═["+colors.reset+"email html file(.txt)"+colors.red+"]")
email_html=input("            ╚══● "+colors.green)
clearConsole()
print(menu)
print(center(pub))
print()
f = open(list, 'r')
text=f.readlines()
NumberOfLine = len(text)
print(NumberOfLine)
email_number= -1
while email_number != NumberOfLine:
    try:
        email_number= email_number+1
        with open(list) as f:
            email = f.readlines()[email_number].rstrip()

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = email
        f = open(email_html, 'r')
        html = f.read() 
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        mail = smtplib.SMTP(server, port)
        mail.ehlo()
        mail.starttls()
        mail.login(id, password)
        mail.sendmail(sender, email, msg.as_string())
        print(colors.green+"[ "+email+" ] >>> email sent !")
        mail.quit()
        f.close()
    except:
        print(colors.red+"["+email+"] >>> sending failed")

try:
    print()
    print("the message was sent to "+email_number+" people !")
    input()
except:
    print()
    print("the message was sent to "+email_number+" people !")
    input()
