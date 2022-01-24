from datetime import datetime

from flask import Flask
from slack_sdk import WebClient

import config
import notion

app = Flask(__name__)
client = WebClient(token=config.SLACK_TOKEN)

members = {
    '4ea6a220-baf0-4998-9678-12d8af9d4b3f': 'U01MXLV5S4Q', #Takumi
}


@app.route('/')
def index():
    res = notion.query_notion_db()

    now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    client.chat_postMessage(channel="#takumi-test", text=f'{now} 時点で期限が過ぎているタスクはこちらです！')

    for todo in res['results']:
        user_id = todo['properties']['Owner']['people'][0]['id']
        title = todo['properties']['Project name']['title'][0]['plain_text']
        status = todo['properties']['Status']['select']['name']
        types = []
        for type_ in todo['properties']['Type']['multi_select']:
            types.append(type_['name'])
        start = todo['properties']['start']['date']['start']
        deadline = todo['properties']['deadline']['date']['start']
        client.chat_postMessage(channel="#takumi-test",
                                text=f"<@{members[user_id]}>\n"
                                     f"`タスク名`: {title} \n"
                                     f"`Status`: {status} \n"
                                     f"`Type`: {','.join(types)} \n"
                                     f"`Start`: {start}\n"
                                     f"`Deadline`: {deadline}")

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0')
