import configparser

class MyError():  

  def __init__(self):
    config = configparser.RawConfigParser()
    config.read('ErrorMessages.properties')

  def newError(self, key):
    if(key)
      print(config.get('ParserErrors', key))


  
