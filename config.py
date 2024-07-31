import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:BAC146@localhost/bes_ecom'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') if os.environ.get('SQLALCHEMY_DATABASE_URI') else 'mysql+mysqlconnector://root:BAC146@localhost/bes_ecom'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False
    
    