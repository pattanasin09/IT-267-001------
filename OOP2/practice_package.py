from cusorder.customer import Customer
from cusorder.order import Order

if __name__ == '__main__':
    guest = Customer('Jame','Nontaburi')
    buyorder = Order('15-06-2022','packed')
    print(f'Order of {guest.name} on {buyorder.date} is {buyorder.status} ')
    