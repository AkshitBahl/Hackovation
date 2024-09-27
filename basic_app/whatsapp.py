

from twilio.rest import Client
from decouple import config 
 
# account_sid = config('ACC_SID')
# auth_token = config('AUTH_TOKEN')
account_sid = Config('ACC_SID')
auth_token = Config('AUTH_TOKEN')
client = Client(account_sid, auth_token) 

def send_message(mesg, num):
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',
                                  body= mesg,  
                                  to= f"whatsapp:{num}"
                              ) 
     
    print(message.sid)
