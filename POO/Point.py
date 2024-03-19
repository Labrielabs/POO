class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Cette méthode permet de rendre l'attribut x en privé

    @property # décorateur transforme la méthode x en get_x()
                    # et l'attribut x devient dès lors privé
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x 
   
# Main
p1 = Point(23.4, 24.2)
print(f"x={p1.x},y={p1.y}")
   
   
   
   
   
   