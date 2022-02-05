from dotenv import load_dotenv
import os

load_dotenv()

SLACK_TOKEN = os.getenv('SLACK_TOKEN')
NOTION_VERSION = '2021-08-16'
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DB_ID = os.getenv('DB_ID')

TAKUMI_EMAIL = os.getenv('TAKUMI_EMAIL')
SHUN_EMAIL = os.getenv('SHUN_EMAIL')
KOICHI_EMAIL = os.getenv('KOICHI_EMAIL')
MOROMIN_EMAIL = os.getenv('MOROMIN_EMAIL')
CHISE_EMAIL = os.getenv('CHISE_EMAIL')

TAKUMI_SLACK = os.getenv('TAKUMI_SLACK')
SHUN_SLACK = os.getenv('SHUN_SLACK')
KOICHI_SLACK = os.getenv('KOICHI_SLACK')
MOROMIN_SLACK = os.getenv('MOROMIN_SLACK')
CHISE_SLACK = os.getenv('CHISE_SLACK')
