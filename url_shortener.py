import requests 

url_to_shorten = input("Enter URL to shorten: ")

if not url_to_shorten.startswith(("http://", "https://")):
    url_to_shorten = "https://" +url_to_shorten

api_url = f"http://tinyurl.com/api-create.php?url={url_to_shorten}"

response = requests.get(api_url)
print(f"Original URL: {url_to_shorten}")
print(f"Shortened URL: {response.text}")
