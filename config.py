import os
class Config:
    '''
    General configuration parent class
    '''
    BASE_URL ='https://newsapi.org/v2sources?&apiKey={}'
    NEWS_API_KEY='38d71ea0c25f44a79c92a2e370b3316a'

    pass


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
     Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}