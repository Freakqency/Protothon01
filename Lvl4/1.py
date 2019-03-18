import smtplib
import logging 
def send(username,password,to_addr,sub,msg):
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.set_debuglevel(1)
	server.login(username,password)
	logging.info('Logged in Successfully')
	from_addr='surya.19.1@protosem.tech'
	message = 'Subject: {}\n\n{}'.format(sub,msg)
	server.sendmail(
	   from_addr,
  	   to_addr, 
           message)
	server.quit()

def main():
	username="surya.19.1@protosem.tech"
	password="iyiQ5BM2XuZc"
	to_addr="surya.19.1@protosem.tech"
	sub='New Test'
	msg='This is a new test mail'
	send(username,password,to_addr,sub,msg)
if __name__ == '__main__':
	main()
