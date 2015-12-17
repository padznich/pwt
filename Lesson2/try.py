import urllib2

file = 'Downloaded.html'

urlic = 'https://dev.projectoxford.ai/docs/services/5639d931ca73072154c1ce89/operations/563b31ea778daf121cc3a5fa/console'

response = urllib2.urlopen(urlic)

with open(file, 'w') as html:
    html.write(response.read())




'''
print(response.info())
print('content-type',response.info()['content-type'])
print(response.read()[:350])
print("The URL is: ", response.geturl())
print("This gets the code: ", response.code)
print("Get the length :", len(html))
'''


