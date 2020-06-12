
# Instances of this class act as a sibling to the original 
# order id. It is used by warehouse staff to "move" the "unit"
# from Picking to QA to Packing.
class MovableUnit():

    def __init__( self, mu_code ):

        self.mu_code = mu_code
        self.order_id = None

        self.wave_id = None
        self.picks_left = None # picks remaining
        self.picks_right = None # picks completed
        self.picks = None # all picks regardles of status

    
    def getOrderID( self ):
        if self.order_id is not None:
            return self.order_id


    def assignOrder( self, order_id ):

        if self.order_id is not None:
            print( 'This MU already has an order tied to it.' )
            return

        else:
            self.order_id = order_id


