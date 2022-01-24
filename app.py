from flask import Flask, render_template

import notion

app = Flask(__name__)


@app.route('/')
def index():
    res = notion.query_notion_db()
    return res


if __name__ == '__main__':
    app.run()
