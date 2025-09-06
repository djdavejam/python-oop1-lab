class Book:
    def __init__(self, title, page_count):
        """
        Initialize a Book object with title and page_count
        
        Args:
            title (str): The title of the book
            page_count (int): The number of pages in the book
        """
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page count"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """
        Set the page count with validation
        
        Args:
            value: The page count value to set
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value
    
    def turn_page(self):
        """Turn to the next page with encouraging message"""
        print("Flipping the page...wow, you read fast!")