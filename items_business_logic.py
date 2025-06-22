"""
@Author: Abhishek Amar
@Email: abhishekamarj@gmail.com
@Date: 2025-06-22
"""
"""
This module contains the business logic for different types of items in the Gilded Rose inventory system.
Each item type related logic can be written here in their specific class with its own logic for updating 
the quality and sell-in values.
The logic is encapsulated in classes that inherit from the base `ItemLogic` class.
"""
"""
 I have created a base class for item;s logic
    # Reason for creation base class and making it @abstractmethod 
 ---> This allows us to add more items with specific business logic in the future without changing the existing code.
      Suppose there are some logic which should be common in some cases in that case we can write those logic
      inside our base class and then override the methods in child classes. This way we can avoid code duplication.
      If we have no common logic then we can just use the base class as an interface and override the method 
      in child class and add our specific logic.
       
"""
from abc import abstractmethod  

# This is my base class 
class ItemLogic:
    @abstractmethod
    def items_operation(self, item):
        raise NotImplementedError() 

# Inheriting from base class 
class ConjuredItemLogic(ItemLogic): 
    def items_operation(self, item):
        # Degrade quality by 2 normally, or 4 if sell_in < 0
        item.sell_in -= 1
        degrade = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - degrade)
        return item
