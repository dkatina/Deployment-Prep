
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:BAC146@localhost/bes_ecom'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://dylank:Be4wCWPRvleRBxyQzjux5HIs8NLRXiP9@dpg-cql7sa3qf0us73frf1n0-a.ohio-postgres.render.com/dbecomprep'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False
    
    