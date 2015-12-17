import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print(r.status_code)
print(r.headers['content-type'])

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)