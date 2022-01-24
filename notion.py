import requests

import datetime
import json

import config

url = f'https://api.notion.com/v1/databases/{config.DB_ID}/query'
headers = {
    'Authorization': config.NOTION_TOKEN,
    'Notion-Version': config.NOTION_VERSION,
    'Content-Type': 'application/json'
}
payload = json.dumps({
    "filter": {
        "and": [
            {
                "property": "Status",
                "select": {
                    "does_not_equal": "完了🎉"
                }
            },
            {
                "property": "deadline",
                "date": {
                    "before": datetime.datetime.now().strftime('%Y-%m-%d')
                }
            }
        ]
    }
})


def query_notion_db():
    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()

    # output = {
    #     'response': response.json(),
    #     'totalCount': len(response.json().get('results'))
    # }

    return response.json()
