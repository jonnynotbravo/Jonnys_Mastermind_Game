import requests

response = requests.get(
    "https://www.random.org/integers/?num=4&min=0&max=7&col=4&base=10&format=plain&rnd=new")

if response.status_code == 200:
    data = response.text.strip()  # Remove any extraneous whitespace
    print("Data received:")
    print(data)  # Check Data

    # Convert the received data into a list of integers
    secret_code = list(map(int, data.split()))
else:
    print("Failed to fetch data. Status code:", response.status_code)
    secret_code = []

# Ensure this script can be imported without running the request again
if __name__ == "__main__":
    print(secret_code)
