import os

class Config(onject):
	SECRET_KEY = os.envirn.get('SECRET_KEY') or 'whatever-it-is'
	