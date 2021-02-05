import requests
# get api request link from sunnah.com
url = "https://api.sunnah.com/v1/hadiths/random"

# declaring data dictionary and required header key
payload = "{}"
headers = {'x-api-key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'}

# getting a random hadiths from the api call
hadith_response = requests.request("GET", url, data=payload, headers=headers)

# converting the response data into json format acting as a dictionary
json_hadith_response = hadith_response.json()

# cleaning the data
hadith_collection = json_hadith_response['collection']
hadith_book_number = json_hadith_response['bookNumber']
hadith_topic = json_hadith_response['hadith'][0]['chapterTitle']
hadith_body = json_hadith_response['hadith'][0]['body']

print(f"From Collection of {hadith_collection.title()}")
print(f"Book of {hadith_book_number}")
print(f"Under the topic:{hadith_topic}")
print(f"Hadith:{hadith_body}")