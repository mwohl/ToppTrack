from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'db':"ToppTrack"}
app.config["SECRET_KEY"] = "bawe924nsli5sk35b2c912nks"

db = MongoEngine(app)

if __name__ == '__main__':
	app.run()