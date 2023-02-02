import json
import requests
from credentials import *

def generate_token():
    payload = {
        'grant_type': 'password',
        'client_id': CONSUMER_KEY,
        'client_secret' : CONSUMER_SECRET,
        'username' : USERNAME,
        'password' : PASSWORD + SECURITY_TOKEN
    }
    oauth_endpoint = '/services/oauth2/token'
    response = requests.post(DOMAIN + oauth_endpoint, data=payload)
    return response.json()["access_token"]

access_token = generate_token()

# Define the data for the new contact
contact_data = {
    "FirstName": "Jir",
    "LastName": "Doey",
    "Email": "janee@example.com",
    "Phone": "345-4565-5555"
}

# Make the API call to create the contact
response = requests.post(f'{DOMAIN}/services/data/v52.0/sobjects/Contact/',
                        headers={'Authorization': f'Bearer {access_token}',
                                 'Content-Type': 'application/json'},
                        json=contact_data)
# Check the status code of the response
if response.status_code == 201:
    print('Contact created successfully!')
else:
    print(f'Error creating contact: {response.text}')

