import os

class Config:
    '''
    general configuration parent class
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    


class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://jose:joseotis45@localhost/blog'

    DEBUG = True


config_options = {
    'developmnet':DevConfig,
    'development':ProdConfig,
    'test':TestConfig
}