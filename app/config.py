class Config:
    '''
    PArent class for all general configurations
    '''
    BASE_URL = 'https://newsapi.org/v2/everything?{}&apiKey={}'
    pass

class prodConfig:
    '''
    Child class for production configuration.

    Arguments:
    Config which is the parent class 
    '''
    pass

class DevConfig(Config):
    '''
    Child class for development configuration

     Arguments:
    Config which is the parent class 
    '''

    DEBUG = True
    