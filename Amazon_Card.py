# Write a program to create a class with name 'Card' which should contain 5 data members. 1. id 2. imageUrl 3. deviceType 4. price 5. rating
# Create 3 objects with below data
# Product-1: imageUrl: "Dummy-url 1" deviceType: "Mobile" price: 56000 rating: 4.5
# Product-2: imageUrl: "Dummy-url 2" deviceType: "Laptop" price: 94000 rating: 4.8
# Product-3: imageUrl: "Dummy-url 3" deviceType: "Smart-watch" price: 18000 rating: 3.5

class Card:
  def __init__(self, imageUrl, deviceType, price, rating):
    self.imageUrl = imageUrl
    self.deviceType = deviceType
    self.price = price
    self.rating = rating

  def printDetails(self):
    print("imageUrl:", self.imageUrl)
    print("deviceType:", self.deviceType)
    print("price:", self.price)
    print("rating:", self.rating)

# Creating objects for each product
product1 = Card("Dummy-url 1", "Mobile", 56000, 4.5)
product2 = Card("Dummy-url 2", "Laptop", 94000, 4.8)
product3 = Card("Dummy-url 3", "Smart-watch", 18000, 3.5)

# Printing details of each product
print("Product - 1 :")
product1.printDetails()
print()

print("Product - 2 :")
product2.printDetails()
print()

print("Product - 3 :")
product3.printDetails()
