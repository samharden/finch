#!/usr/bin/env python

import requests
import json
from crm.settings import FASTCASE_API_KEY

def get_citation(volume, reporter, page):
    body = {
    	"Context": {
    		"ServiceAccountContext": FASTCASE_API_KEY,
    	},
    	"Request":{
    		"Citations":[
    			{
    				"Volume": volume,
    				"Reporter": reporter,
    				"Page": page
    			}]}}

    headers = {
                'Content-type': 'application/json',
                'SecurityServices':'AuthenticateServiceAccountContext()'
                }
    response = requests.post(
                "https://services.fastcase.com/REST/ResearchServices.svc/GetPublicLink",
                json = body,
                headers = headers)

    citation_response = json.loads(response.content.decode())
    # print(response.content)
    result = citation_response['GetPublicLinkResult']['Result'][0]['Url']
    print(result)
    return result


if __name__ == '__main__':
    get_citation(1, "US", 1)
