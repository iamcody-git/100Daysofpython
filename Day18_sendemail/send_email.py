import smtplib,ssl
# import os
# from dotenv import load_dotenv

def send_mail(message):
        # load_dotenv()
        # print(f"Loaded password: {os.getenv('PASSWORD')}")
        host = "smtp.gmail.com"
        port = 465

        username = "adhikariprashant009@gmail.com"
        password = "xtam whvf yofo zcdg"

        receiver = "iamcody.github@gmail.com"
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username,password)
            server.sendmail(username,receiver,message)