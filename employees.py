

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


class MovableUnit():
    def __init__( self ):
        self.orderID = None


class Order():



class Cart():
    def __init__( self, orders ):
        self.orders = {order.id: order for order in orders}

    def getOrders( self ):
        return self.orders

    def addOrder( self, order ):
        if self.orders is None:
            self.orders = {}

        self.orders[order.id] = order

    
    def removeOrder( self, order ):

        if self.orders.get( order.id ) is not None:
            del self.orders[order.id]

    







if __name__ == '__main__':

    test = Picker( 1234, 'billy', 'picker' )
    test.test()
