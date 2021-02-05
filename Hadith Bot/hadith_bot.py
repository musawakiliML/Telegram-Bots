import requests
# get api request link from sunnah.com
url = "https://api.sunnah.com/v1/hadiths/random"

payload = "{}"
headers = {'x-api-key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'}

hadith_response = requests.request("GET", url, data=payload, headers=headers)

json_hadith_response = hadith_response.json()

print(json_hadith_response)
