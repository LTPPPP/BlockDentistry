import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key'
    BLOCKCHAIN_DIFFICULTY = '0000'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    BLOCKCHAIN_DIFFICULTY = '00'  # Easier difficulty for testing

class ProductionConfig(Config):
    # Production-specific configs
    pass

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}