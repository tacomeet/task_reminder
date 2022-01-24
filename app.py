from datetime import datetime

from flask import Flask
from slack_sdk import WebClient

import config
import notion

app = Flask(__name__)
client = WebClient(token=config.SLACK_TOKEN)

members = {
    config.TAKUMI_EMAIL: config.TAKUMI_SLACK,
    config.SHUN_EMAIL: config.SHUN_SLACK,
    config.KOICHI_EMAIL: config.KOICHI_SLACK,
    config.MOROMIN_EMAIL: config.MOROMIN_SLACK,
    '': ''
}


@app.route('/')
def index():
    res = notion.query_notion_db()

    now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    client.chat_postMessage(channel="#task", text=f'{now} 時点で期限が過ぎているタスクはこちらです！')

    for todo in res['results']:
        try:
            user_email = todo['properties']['Owner']['people'][0]['person']['email']
        except TypeError:
            user_email = ''
        try:
            title = todo['properties']['Project name']['title'][0]['plain_text']
        except TypeError:
            title = ''
        try:
            status = todo['properties']['Status']['select']['name']
        except TypeError:
            status = ''
        types = []
        for type_ in todo['properties']['Type']['multi_select']:
            types.append(type_['name'])
        try:
            start = todo['properties']['start']['date']['start']
        except TypeError:
            start = ''
        deadline = todo['properties']['deadline']['date']['start']
        client.chat_postMessage(channel="#task",
                                text=f"<@{members[user_email]}>\n"
                                     f"`タスク名`: {title} \n"
                                     f"`Status`: {status} \n"
                                     f"`Type`: {','.join(types)} \n"
                                     f"`Start`: {start}\n"
                                     f"`Deadline`: {deadline}")

    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
