class Card:  
    def __init__(self, color, value):  
        self.color = color  
        self.value = value  

    def __str__(self):  
        return f'{self.value} {self.color}'  
