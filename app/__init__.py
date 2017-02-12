from flask import Flask
import wolframalpha
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

app = Flask(__name__)
#app.config.from_object('app.config')
#app.config.from_envvar('YOURAPPLICATION_SETTINGS')
#db = SQLAlchemy(app)
#login_manager = LoginManager()
#login_manager.init_app(app)
app_id = 'P7L7Q6-XX24PXPHG5'
client = wolframalpha.Client(app_id)


from app import views, models