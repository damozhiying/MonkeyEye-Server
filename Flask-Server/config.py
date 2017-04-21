class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 15
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False
    SESSION_REFRESH_EACH_REQUEST = False
    SESSION_COOKIE_SECURE = True

    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'default': DevelopmentConfig
}
