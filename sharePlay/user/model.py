# virtualize databse
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..model.model import db, ma

class User(db.Model):
    tablename = 'user'

    user_id = db.Column(db.Integer,primary_key=True, nullable=False)
    user_name = db.Column(db.String(30))

    def init(self):
        super().init()

    def repr(self):
        return 'User {}, {}'.format(self.user_id, self.user_name)

class User_schema(SQLAlchemyAutoSchema):
    class Meta:
        fields = ('user_id', 'user_name')