import requests

url = "https://www.random.org/integers/?num=4&min=0&max=7&col=4&base=10&format=plain&rnd=new"

response = requests.get(url)

if response.status_code == 200:
    data = response.text
    print("Data received:")
    print(data)
else:
    print("Failed to fetch data. Status code:", response.status_code)
