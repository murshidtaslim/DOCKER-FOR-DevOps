import urllib.request

# Bina kisi IP address ke seedha server container ka naam 'my-server' use kar rahe hain
url = "http://my-server:5000"

response = urllib.request.urlopen(url)
message = response.read().decode("utf-8")
print("Client ko mila jawab ->", message)
