import yaml


def fetchIpAddress (configFileName, appliance):
    with open("config.yaml", 'r') as stream:
        try:
            obj = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
    return obj["config"][appliance]["ip"]

def fetchToken (configFileName, appliance):
    with open("config.yaml", 'r') as stream:
        try:
            obj = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
    return obj["config"][appliance]["token"]