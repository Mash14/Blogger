# Where we will store our app configurations.
import os

class Config:
    '''
    General configurations parent class
    '''
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # for forms csrf 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production configurations child class

    Args:
        Config: The parent configuration class with 
        General configurations settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    '''
    Development configurations child class

    Args:
        Config: The parent configuration class 
        with General configurations settings
    '''
    # database link
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mash:password@localhost/personalblog'
    DEBUG = True

class TestConfig(Config):
    '''
    Test  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:password@localhost/personalblog_test'

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}