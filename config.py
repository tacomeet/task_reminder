from dotenv import load_dotenv
import os

load_dotenv()

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
NOTION_VERSION = '2021-08-16'
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DB_ID = os.getenv('DB_ID')
