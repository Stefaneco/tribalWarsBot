
import json
import requests

webhook_gang = "https://discordapp.com/api/webhooks/596814508459294730/dR1PWAoZIKikJ3G7BDwL8LV7wTysmZwHFWBkp0z1I6kjuRRykYuc4ukXFUdjTJ4PVSpe"
webhook_server = "https://discordapp.com/api/webhooks/597742331164098590/KMOSLZTEytHZ6Y0aOU0JTa3aBMWnjuCZqB3kD_DrQJpcZjgntCKkBdRpOI-1CNVZBHGd"

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

