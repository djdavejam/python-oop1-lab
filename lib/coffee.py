class Coffee:
    def __init__(self, size, price):
        """
        Initialize a Coffee object with size and price
        
        Args:
            size (str): The size of the coffee (Small, Medium, or Large)
            price (float): The price of the coffee
        """
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Get the coffee size"""
        return self._size
    
    @size.setter
    def size(self, value):
        """
        Set the coffee size with validation
        
        Args:
            value: The size value to set
        """
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
        self._size = value
    
    def tip(self):
        """
        Add a tip to the coffee price
        Increases the price by 1 and prints a thank you message
        """
        print("This coffee is great, here's a tip!")
        self.price += 1