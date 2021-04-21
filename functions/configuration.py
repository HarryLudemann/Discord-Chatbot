# This file Controls Config Functions (Create, Get, Set)
from configparser import ConfigParser

# Create Config File
def CreateConfigFile():
    #Get the configparser object
    config_object = ConfigParser()
    #Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
    config_object["MAIN"] = {
        "identifier": "$"
    }
    config_object["PRIVILEGES"] = {
        "fun-inspire": "@everyone",
        "fun-comeback": "@everyone",
        "fun-cat": "@everyone",
        "fun-dog": "@everyone",
        "basic-ping": "@everyone",
        "admin-quit": "Admin",
        "chatbot-chat": "@everyone",
        "chatbot-train": "@everyone",
        "chatbot-askquestion": "@everyone",
        "chatbot-listintents": "@everyone"

    }
    #Write the above sections to config.ini file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

# Get Saved Config Value
def GetConfigValue(Value, Section):
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    #Create Object Of ServerSettings
    ServerSettings = config_object[Section]
    return ServerSettings[Value]

# Set Config Value to file
def SetConfigValue(Value, NewValue, Section):
    config_object = ConfigParser()
    config_object.read("config.ini")
    #Create Object Of ServerSettings
    ServerSettings = config_object[Section]
    #Update the value
    ServerSettings[Value] = NewValue
    #Write changes back to file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

if (__name__ == "__main__"):
    CreateConfigFile()
