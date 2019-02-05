# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Aljumiah Store"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for storeList in stores:
        print(storeList.name)
    
def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store.name == store_name:
            return store
        
    return False


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
 
    pick_store = input("Please Pick a store: ")
    while pick_store != "checkout":
        if get_store(pick_store):
            return get_store(pick_store)
        else:
             print("invalid, try again ")
    return "checkout"

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
    pick_product_input = input("Pick the item you would like to add: ")
    while pick_product_input.lower() != "back":
        for product in picked_store.products:
            if product.name == pick_product_input:
                cart.add_to_cart(product)
        
        pick_product_input = input("what else would you like? ")
    return "checkout"

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    store_picked = pick_store()
    while store_picked != "checkout":
        pick_products(cart,store_picked)
        store_picked = pick_store()
    cart.checkout()
    
def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
