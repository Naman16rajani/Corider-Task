from flask import Flask
from routes.user_routes import user_routes
from mongoengine import connect
from pymongo import MongoClient

app = Flask(__name__)
app.register_blueprint(user_routes)

app.config.from_object('config.Config')
pool_size = 10

client = MongoClient(app.config['MONGO_URI'], maxPoolSize=pool_size)

# connect(app.config['USER_DB'], host=client)
connect('users', host=app.config['MONGO_URI'])

if __name__ == '__main__':
    app.run(debug=True)
