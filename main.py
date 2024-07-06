from datetime import datetime
from dotenv import load_dotenv
import os
import requests

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
TOKEN = os.getenv('TOKEN')

USERNAME = "johlstrom"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

def show_menu():
    print("Please select an option:")
    print("0. Coding")
    print("1. Walking")
    print("2. Other Exercise")
    print("3. Golf")
    print("4. Swedish")

def get_selection():
    valid_choices = {
        '0': 'Coding', 
        '1': 'Walking', 
        '2': 'Other Exercise', 
        '3': 'Golf', 
        '4': 'Swedish'
    }
    while True:
        show_menu()
        choice = input("Enter the number corresponding to your choice: ")
        if choice in valid_choices:
            return choice
        else:
            print("Invalid selection. Please try again.")

def get_date():
    today = datetime.now().strftime('%Y%m%d')
    date_str = input(f"Enter the date (yyyymmdd) [default: {today}]: ")
    if not date_str:
        date_str = today
    try:
        datetime.strptime(date_str, '%Y%m%d')  # validate date format
    except ValueError:
        print("Invalid date format. Please try again.")
        return get_date()
    return date_str

def get_quantity(option):
    unit = {
        '0': 'minutes',
        '1': 'kilometers',
        '2': 'minutes',
        '3': 'minutes',
        '4': 'minutes'
    }[option]
    quantity_str = input(f"Enter the quantity in {unit}: ")
    return quantity_str

def process_selection(selection_id, date, quantity):
    print(f"Processing selection:")
    print(f"ID: {selection_id}")
    print(f"Date: {date}")
    print(f"Quantity: {quantity}")
    post_config = {
        "date": date,
        "quantity": quantity
    }
    post_endpoint = f"{GRAPH_ENDPOINT}/graph{selection_id}"
    print(post_endpoint)
    response = requests.post(url=post_endpoint, json=post_config, headers=headers)
    print(response.text)

# Main function to run the menu and get additional inputs
def main():
    option = get_selection()
    date = get_date()
    quantity = get_quantity(option)
    print(option)
    print(date)
    print(quantity)
    process_selection(option, date, quantity)

# Run the main function
if __name__ == "__main__":
    main()