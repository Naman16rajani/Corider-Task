import datetime
from mongoengine import Document, StringField, IntField

class UserModel(Document):
    id = IntField( alias='_id', primary_key=True, unique=True, required=True)
    name = StringField(required=True)
    email = StringField(
        required=True, 
        unique=True,
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 
        )
    password = StringField(required=True, min_length=6, max_length=16, regex=r'^[a-zA-Z0-9_.+-]+$')
    def default_id():
        return int(datetime.datetime.now().timestamp())
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    meta = {
        'collection': 'users'
    }


class User():
    _userModel = None
    def __init__(self):
        if not self._userModel:
            self._userModel =  UserModel
       

    def create_user(self, user_data):
        if 'id' not in user_data:
            user_data['id'] = self._userModel.default_id()
        return self._userModel(**user_data).save().to_json()
    
    def get_all_users(self):
        users = self._userModel.objects.all()
        return users
    
    def get_user(self, user_id):
        user = self._userModel.objects.get(id=user_id)
        return user.to_json()

    def update_user(self, user_id, user_data):
        result = self._userModel.objects.get(id=user_id)
        result.name = user_data['name']
        result.email = user_data['email']
        result.password = user_data['password']
        result.save()
        return result.to_json()

    def delete_user(self, user_id):
        result = self._userModel.objects.get(id=user_id)
        if result:
            result.delete()
            return "user deleted"
        else:
            result = None
            return "already deleted"
