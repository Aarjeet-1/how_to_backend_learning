from os import path
from flask import  Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager     




db = SQLAlchemy ()
DB_Name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ygfvttyu ihnb'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'

    db.init_app(app)
    
  



    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User , Note
    login_manager = LoginManager()

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
       return User.query.get(int(id))
       

    database_create(app)


    return app
def database_create(app):
    if not path.exists('web/' + DB_Name):
        # db.create_all(app=app)
        
        print('Database created ...')

