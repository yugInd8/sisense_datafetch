import requests

# Sisense instance URL and API Key
API_URL = 'your url sisense.com/api/v1'
API_KEY = 'your api key'

# Headers for API requests
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Function to fetch and print all unique attributes from the dashboards response
def print_attributes(data):
    if isinstance(data, list):
        # Loop through the list and print attributes of each dictionary
        for item in data:
            if isinstance(item, dict):
                print("Attributes:", item.keys())
            elif isinstance(item, list):
                # Recursively handle nested lists
                print_attributes(item)
    elif isinstance(data, dict):
        # Handle dictionary and print attributes
        print("Attributes:", data.keys())
        # Recursively handle nested dictionaries
        for key, value in data.items():
            print_attributes(value)

# Fetch a list of dashboards and print their attributes
def fetch_dashboards():
    response = requests.get(f'{API_URL}/dashboards', headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Dashboard Data Attributes:")
        print_attributes(data)
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Fetch data from a specific dashboard and print its attributes
def fetch_dashboard_data(dashboard_id):
    response = requests.get(f'{API_URL}/dashboards/{dashboard_id}/widgets', headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Dashboard Data for ID {dashboard_id} Attributes:")
        print_attributes(data)
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print(response.text)  # Print the response body for more details
        return None

# Example usage
fetch_dashboards()
fetch_dashboard_data('your_dashboard_id')  # Replace 'your_dashboard_id' with an actual ID
