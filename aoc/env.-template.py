"""Config file"""
_config_vars = {"AOC_SESSION": "AOC session cookie",
          "CACHE": "./cache/"}

def config(var):
    """Returns config var"""
    return _config_vars.get(var)
