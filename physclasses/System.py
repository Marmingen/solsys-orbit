#################################################################################
## SYSTEM CLASS

class System():
    
    def __init__(self):
        
        self.bodies = {}
    
    def add_body(self, body):
        self.bodies[body.name] = body