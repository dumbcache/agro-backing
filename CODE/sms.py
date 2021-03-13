import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

def sendSms(args):
  number=args['farmerMobile'].lstrip('Mobile:')
  farmername=args['farmerName'].lstrip('Name:')
  message="Agro-Backing\n hey "+farmername+"Looking forward to hear from you. \n name: "+args['name']+"\n"+"mobile: "+args['phno']

  # get response
  response = sendPostRequest(URL, '8HGNN4X47OT6DE6U4TL3W8NN65HEA041', 'HBBZG2AVMS9FS057', 'stage', number, 'active-sender-id', message )

  # print(response.text)
  return

if __name__=='__main__':
  pass
