# 01 - The happy path. No error handling at all.
# Break it: misspell USER, or turn off Wi-Fi, and read the traceback.

import httpx
import json

USER = "schaconx" 
URL = "https://api.github.com/users/{user}/events/public"
try: 
    response = httpx.get(URL.format(user=USER))
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    data = response.json()
# print(json.dumps(data, indent=2))
# structured data is a parquet file (one schema, tidy structure)
# unstructured data normally uses JSON because the data doesn't conform to one schema 
    for item in data: 
        print(item["repo"]["name"], " - ", item["type"])
except httpx.HTTPError as e:
    print(e)