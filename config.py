
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:BAC146@localhost/bes_ecom'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:BAC146@localhost/bes_ecom'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False
    
    