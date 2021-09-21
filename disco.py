
import json
import requests

webhook_gang = "https://discordapp.com/api/webhooks/XXXXXX"
webhook_server = "https://discordapp.com/api/webhooks/XXXXXX"

def sendWeebhook(webhook_url, message):
	payload = {
		"content": message
	}
	headers = {
		"Content-Type": "application/json",
	}
	response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
	return response

def send(msg):
	sendWeebhook(webhook_server, msg)

