from pathlib import Path

resource_path = ''

def prepareResourcePath():
    global resource_path
    resource_path = str(Path(__file__).parent.joinpath('..', 'resource'))
 
def getResource( res : str):
    return (resource_path + '/' + res)
