class Config:
    '''
    General configuration parent class
    '''
    pass



class DevConfig(Config):
    '''
     Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    BASE_URL ='https://newsapi.org/v2sources?&apiKey={}'
    pass


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True