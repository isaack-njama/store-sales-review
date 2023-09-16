from functools import reduce

'''
Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

The owner wants you to do some calculations on the data with these criteria's:

    -calculate the total price average for all products

    -create a new price list that reduces the old prices by $ 5

    -calculate the total revenue generated from the products

    -calculate the average daily revenue generated from the products

    -based on the new prices, which products are less than $ 30 

Below is the data you are to use for the problem :

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
'''

def store_sales_review(products, prices, last_week):
    products_length = len(products)
    prices_length = len(prices)
    last_week_length = len(last_week)

    # Compute total price average for all products
    total_price_average = reduce(lambda x, y: x + y, prices) / prices_length
    print(total_price_average)

    # Reduce old prices by $5
    new_price_list = list(map(lambda x: x - 5, prices))
    print(new_price_list)

    # Compute total revenue generated from products
    total_revenue = reduce((lambda x, y: x * y), [prices, last_week])
    print(total_revenue)


products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
res = store_sales_review(products, prices, last_week)
print(res)