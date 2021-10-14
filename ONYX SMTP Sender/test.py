import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class colors:
    red = "\033[31m"
    yellow = "\33[33m"
    green = "\33[92m"
    purple = "\033[35m"
    reset = "\33[37m"
me = "esio.yt.04@gmail.com"
you = "dsfgdhygtyjuiyfiedtgbgfju@yopmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Paypal service"
msg['From'] = me
msg['To'] = you

f = open('email_html.txt', 'r')
html = f.read() 

part2 = MIMEText(html, 'html')
msg.attach(part2)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('esio.yt.04@gmail.com', 'travailler')
mail.sendmail(me, you, msg.as_string())
print(colors.green+"the html email was successfully sent !")
input()
mail.quit()
f.close()