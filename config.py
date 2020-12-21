class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/flask_tdd'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET = "\xd1\xd7\xee_\xab\xd0UB:\x18\x1bh8\xc8\x90\x0eb+\xc67R\xec^\x90"
    TOKEN_EXPIRES = 300  # in seconds


class ProductionConfig(Config):
    pass
    

class DevelopmentConfig(Config):
    DEBUG = True
    pass

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/test'
