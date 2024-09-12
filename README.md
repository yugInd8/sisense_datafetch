# Fetching data from Sisense APIs

This repository is aimed at fetching and exploring data using Sisense REST APIs. As of now, it is on very initial stage of exploring the API.

## Scripts

### 1. `test.py`

This script is designed to:
- Fetch a list of dashboards from Sisense.
- Fetch widgets data from a specific dashboard.

#### How to Use:
1. Replace `API_URL` and `API_KEY` in the script with a valid dashboard ID.
2. Run the script:
   ```bash
   python test.py
   ```

### 2. `test_atts_list.py`

This script fetches data from Sisense and prints all unique attributes present in the API's JSON response. It's useful for understanding the structure of data returned by the API.

#### How to Use:
1. Replace `API_URL` and `API_KEY` with an actual dashboard ID.
2. Run the script:
   ```bash
   python test_atts_list.py
   ```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yugInd8/sisense_datafetch.git
   cd sisense_datafetch
   ```

2. **Install Dependencies**:
   Make sure you have Python installed and install the dependencies by running:
   ```bash
   pip install requirements.txt
   ```

3. **Set up Sisense API Key**:
   Update the `API_KEY` and `API_URL` values in the scripts with your actual Sisense API key and instance URL.

## Notes
- **Error Handling**: The scripts will print status codes and response bodies for any failed API calls to help troubleshoot issues.

## Contribution

Feel free to fork the repository, open issues for bugs, or suggest improvements. The idea behind this repo is to explore the knowhows of using Sisense's APIs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Just copy and paste the above text directly into the `README.md` edit page!
