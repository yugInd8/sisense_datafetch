import requests

# Sisense instance URL and API Key
API_URL = 'your url /sisense.com/api/v1'
API_KEY = 'your api key'

# Headers for API requests
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Example: Fetch a list of dashboards
def fetch_dashboards():
    response = requests.get(f'{API_URL}/dashboards', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Example: Fetch data from a specific dashboard
def fetch_dashboard_data(dashboard_id):
    response = requests.get(f'{API_URL}/dashboards/{dashboard_id}/widgets', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print(response.text)  # Print the response body for more details
        return None


# Fetch and print dashboards
dashboards = fetch_dashboards()
if dashboards:
    print(dashboards)

# Fetch and print data from a specific dashboard (replace 'dashboard_id' with an actual ID)
dashboard_data = fetch_dashboard_data('your_dashboard_id')
if dashboard_data:
    print(dashboard_data)
