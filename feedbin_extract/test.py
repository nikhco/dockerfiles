import requests
import base64
from hashlib import sha1
import hmac
from pprint import pprint

username = "username"
secret = "secret"
protocol = "http://"
host = "localhost"
port = "3000"
url = "https://feedbin.com/blog/2018/09/11/private-by-default/"

hashed = hmac.new(secret, url, sha1)

hex_digest = hashed.hexdigest()

base64_url = base64.b64encode(url)

response = requests.get(protocol + host + ":" + port + "/parser/" + username + "/" + hex_digest + "?base64_url=" + base64_url)

print response
pprint(response.content)
