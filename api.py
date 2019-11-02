
import requests
import json
identity = "Group5"
token = "865b22aa-aa80-4fb0-83f0-53e5133f3603"
customerID = '2'
accountID = '0'

def test():
    #customer details
    cusdetails = requests.get("http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/{}/details".format(accountID),headers = {"identity": identity, "token": token})
    details = json.loads(cusdetails.text)

    test1()

