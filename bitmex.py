import requests
import json
"""
https://www.bitmex.com/api/explorer/
"""


def getTrade(count):
	api = 'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&columns=side%2Csize%2Cprice&count={cnt}&reverse=true'
	url = api.format(cnt=count)
	rq = requests.get(url)
	data = json.loads(rq.text)
	return data
