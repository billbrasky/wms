import yaml

# Reads a YAML file
def getYAML( source: str ) -> dict:
    with open( source + '.yml', 'r' ) as f:
        data = yaml.load( f )
    return data
