import logging

class BridgeConfig:
    __instance = None
    __config = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if BridgeConfig.__instance == None:
            BridgeConfig()
        return BridgeConfig.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if BridgeConfig.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BridgeConfig.__instance = self
    
    @classmethod
    def setConfig(obj, config):
        logging.debug('BridgeConfig: set config')
        obj.__config = config
    
    @classmethod
    def getConfig(obj):
        logging.debug('BridgeConfig: get config')
        return obj.__config

    @classmethod
    def getPartialConfig(obj, part):
        logging.debug('BridgeConfig: get ' + part)
        return obj.__config[part]

    @classmethod
    def updateLightState(obj, id, newState):
        logging.debug('BridgeConfig: light update ' + id)

        obj.__config["lights"][id]["state"].update(newState)
