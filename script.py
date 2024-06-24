# Download the helper library from https://www.twilio.com/docs/python/install
import os
import random

from twilio.rest import Client
from dotenv import load_dotenv 

#Load environmental variables
load_dotenv() 

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('SID')
auth_token = os.getenv('AUTH')
client = Client(account_sid, auth_token)

def randomPregnancyIntro():
    message = ['Hello! I think I am pregnant. Can you help?', 'I am worried I might be pregnant.', 'I am looking for an abortion. Can you help?',
    'Hello. I am scared I might be pregnant.', 'Do you all do adoptions?', 'What kind of services do you offer?',
    'I am looking to volunteer!', 'I am hoping to donate to you all! Do you have a website or person to contact?','What is your website?'
    'How are you today? I think I might be pregnant. Do you have any resources?'
    
    
    
    
    
    ]
    return (random.choice(message))


#Ability to change message 
message = client.messages \
                .create(
                     body=randomPregnancyIntro(),
                     from_='+13306484254',
                     to='+19152675166'
                 )



print(message.sid)