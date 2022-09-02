import requests
import json

def lookup(number):
	"""simple function that looks up the phone number via an api"""
	API_KEY = '79416243fc98c8c8dbc88b874adfdb57'
	# sets payload, sends request to the api and returns the json
	payload = {'secret_key': API_KEY, 'number': number}
	r = requests.get('https://numverify.com/php_helper_scripts/phone_api.php', params=payload)

	# decodes the json and prints the data in a nice format
	for key, value in json.loads(r.text).items():
		print(key + ':', value)

if __name__ == '__main__':
	phone_number = input('Please enter the phone number: ')
	lookup(phone_number)
	input('Press enter to exit...')