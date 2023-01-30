from flask import Flask, request
import json
import os
import xmltodict


"""
to run the app use python3 webhook.py
"""

app = Flask(__name__)

@app.route('/contact', methods = ['POST'])
def create_contact_webhook():
   # contact = request.get_json()
    data = request.data
    
    # Convert the XML data to a Python dictionary
    data_dict = xmltodict.parse(data)
    
    # Extract the contact information from the dictionary
    email = data_dict['soapenv:Envelope']['soapenv:Body']['notifications']['Notification']['sObject']['sf:Email']
    first_name = data_dict['soapenv:Envelope']['soapenv:Body']['notifications']['Notification']['sObject']['sf:FirstName']
    last_name = data_dict['soapenv:Envelope']['soapenv:Body']['notifications']['Notification']['sObject']['sf:LastName']
    print(email)
    # 
    
    # Call the function to create a new subscriber in Mailchimp
    # You can replace it with any other function you want to carry out when the webhook is received
    # This can be storing the new contact in a database, syncing with a mailing list, or updating an internal system
   # create_mailchimp_subscriber(email, first_name, last_name)

    return "Success", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port= int(os.environ.get('PORT', 5000)))

