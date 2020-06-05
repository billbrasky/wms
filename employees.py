

class Employee:
    def __init__( self , id, name, function ):
        self.id = id
        self.name = name
        self.function = function

class Picker( Employee ):
    def test( self ):
        print( self.id, self.name, self.function )


    def basicPicker( self ):

        self.zones = ['zoneA', 'zoneB']


    def trustedPicker( self ):

        self.zones = self.basicPicker + ['lockup']

    def southPicker( self ):

        self.zones = self.basicPicker + ['south']

    def adminPicker( self ):

        self.zones = set( self.trustedPicker + self.southPicker )






if __name__ == '__main__':

    test = Picker( 1234, 'billy', 'picker' )
    test.test()
