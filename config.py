class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite:///:memory:'
    JWT_SECRET = "\xd1\xd7\xee_\xab\xd0UB:\x18\x1bh8\xc8\x90\x0eb+\xc67R\xec^\x90"
    TOKEN_EXPIRES = 300  # in seconds

class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
