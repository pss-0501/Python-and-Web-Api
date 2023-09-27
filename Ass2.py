
import requests


# Login when program starts
#bu_id = 'B01022274'
username = "psawant4"
password = "2274@psawant4"

login_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/auth/signin'
login_payload = {'username': username, 'password': password}

# Login Code
response = requests.post(login_url, json=login_payload)
if response.status_code == 200:
    token = response.json().get('authToken')            # Get Token
    headers = {'Authorization': f'Bearer {token}'}      # Token passed to header
    print('Login Success!')
else:
    print('Login failed')
    exit()

# Get Cart details
def GetCartDetails(headers):
    cart_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/cart'
    #data = 'productId'
    response = requests.get(cart_url, headers=headers)          # Get response from API
    if response.status_code == 200:
        cart_data = response.json()
        # Extract and print information about the items in the cart
        print('\n')
        print('Cart Details: ')
        print(cart_data)
    else:
        print('Failed to get cart')

def DeleteCart(headers):
    user_input = input('Enter product ID for delete or Enter no to stop delete: ')      # Delete Cart Data
    if(user_input != 'no'):             # to stop delete
        cart_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/cart'
        data = {'productId':user_input}
        response = requests.delete(cart_url, headers=headers, json=data)        # Get delete response
        if (response.status_code == 200):
            print('Cart emptied successfully')
        else:
            print('Failed to empty cart')
    else:
        print('Delete method stopped!')

def GetProducts(headers):               # Check products
    products_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/products'
    response = requests.get(products_url, headers=headers)
    if response.status_code == 200:
        products_data = response.json()
        # Extract product IDs for items you want to add to the cart
        print('\n')
        print('Product Details: ')
        print(products_data)
    else:
        print('Failed to fetch product data')
        exit()

def AddToCart(headers):         # To add to the cart
    prod_id = input('Enter product ID: ')
    add_to_cart_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/cart'
    cart_payload = {'productId': prod_id}  
    response = requests.post(add_to_cart_url, json=cart_payload, headers=headers)
    if response.status_code == 200:
        print('Items added to cart successfully')
    else:
        print('Failed to add items to cart')

def UpdateCart(headers):    # update cart quantity for each product
    print('\n')
    prod_id = input('Enter product ID: ')
    quantity = int(input('Enter the amount of quantity: '))
    update_cart_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/cart/update'
    cart_update_payload = {'productId': prod_id, 'quantity': quantity}  # Replace with the desired product and quantity
    response = requests.patch(update_cart_url, json=cart_update_payload, headers=headers)
    if response.status_code == 200:
        print('Cart updated successfully')
    else:
        print('Failed to update cart')

def GetOrderDetails(header):
    order_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/orders'       # check placed orders
    response = requests.get(order_url, headers=headers)
    if response.status_code == 200:
        order_data = response.json()
        # Extract product IDs for items you want to add to the cart
        print('\n')
        print('Order Details: ')
        print(order_data)
    else:
        print('Failed to fetch order data')
        exit()


def PlaceOrder(headers):
    checkout_url = 'http://sysrev1.cs.binghamton.edu:9090/api/v1/orders'        # for placing order post method
    response = requests.post(checkout_url, headers=headers)
    if response.status_code == 200:
        print('Order placed successfully')
    else:
        print('Failed to place order')


#Loop to added

while True:
    print('\n')             # Switch Case for choosing the what API function to call
    selected_key = input("Enter a key (0 for Exit, 1 for Cart Details, 2 for Delete Cart, 3 for Product Details, 4 for Add product to cart, 5 for Updating Cart Quantity, 6 for Order Details, 7 for Placing Order): ")
    selected_key = int(selected_key)
    # Create a case that maps keys to functions

    match selected_key:
        case 0:
            print('Exiting the program')
            exit()
            False
        case 1:
            GetCartDetails(headers)
        case 2:
            DeleteCart(headers)
        case 3:
            GetProducts(headers)
        case 4:
            AddToCart(headers)
        case 5:
            UpdateCart(headers)
        case 6:
            GetOrderDetails(headers)
        case 7:
            PlaceOrder(headers)
        case default:
            print("Invalid key - Please try again!")

