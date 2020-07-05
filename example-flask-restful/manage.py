import os
from os.path import join
from dotenv import load_dotenv
from app import create_app

dotenv_path = join(os.getcwd(), '.env')
load_dotenv(dotenv_path)
config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)
if __name__ == '__main__':
    app.run()
