
class Config():
    TESTING = False
    SECRET_KEY = '\x01\xc8$\x97\xd9\x1a\x13\xd9\x9eE\xabS\xc8\x17\xa4\xc3\x14\xe8Re\x94\x8cKR'

class ProductionConfig(Config):
    DEBUG = False
    MAIL_SERVER = ""
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

class MailData():
	FROM = 'araikc@gmail.com'
	TO = ['araikc@yahoo.com']
