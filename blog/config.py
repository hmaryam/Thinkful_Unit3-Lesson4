import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://hmaryam:thinkful@localhost:5432/blogful"
    DEBUG = True

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/blogful-test"
    DEBUG = False
    SECRET_KEY = "Not secret"