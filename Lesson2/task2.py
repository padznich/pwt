s = 'https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair+=+%22USDRUB,EURRUB%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='


def parse(s):
    import urllib2
    import json

    u = urllib2.urlopen(s)
    u.getcode()
    data = u.read()
    u.close()


    #import pprint
    parse_data = json.loads(data)
    #pprint.pprint(parse_data)

    print('_'*40)
    for i in range(len(parse_data['query']['results']['rate'])):
        print(parse_data['query']['results']['rate'][i]['Name'],
              parse_data['query']['results']['rate'][i]['Rate'])
        print('_'*40)

parse(s)