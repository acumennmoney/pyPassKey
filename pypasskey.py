import json
import os


def save_credentials(service, username, password):
	credentials = {}
	if os.path.exists('credentials.json'):
		with open('credentials.json', 'r') as file:
			try:
				credentials = json.load(file)
			except json.JSONDecodeError:
				credentials = {}
	credentials[service] = {'username': username, 'password': password}
	with open('credentials.json', 'w') as file:
		json.dump(credentials, file)


def get_credentials(service):
	if os.path.exists('credentials.json'):
		with open('credentials.json', 'r') as file:
			credentials = json.load(file)
		if service in credentials:
			return credentials[service]
	return None
