import sys
import json
if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

URL_SEARCH_MANUAL = 'http://munchii.me/unitydocs/manual.json'
URL_SEARCH_SCRIPT = 'http://munchii.me/unitydocs/script.json'
    
class DocsResult (object):
  def __init__ (self, title, description, url):
    self.title = title
    self.description = description
    self.url = url

  def __str__ (self):
    return '%s: %s (%d)' % (self.title, self.description, self.url)

def get_search_json (docs):
  if docs == "script":
    #script = open('UnityDocs/script.json', 'r')
    script = urlopen(URL_SEARCH_SCRIPT).read()
    #jsonData = json.load(script)
    jsonData = json.loads(script)
    script.close()
  else:
    #manual = open('UnityDocs/manual.json', 'r')
    manual = urlopen(URL_SEARCH_MANUAL).read()
    #jsonData = json.load(manual)
    jsonData = json.loads(manual)
    manual.close()

  return jsonData

def parse_search_json (searchItem, json):
  results = []

  for element in json:
    if searchItem in element['title']:
      result = DocsResult(str(element['title']), str(element['description']), str(element['link']))
      results.append(result)

  return results[0]

def search (search, docs):
  json = get_search_json (docs)
  return parse_search_json (search, json)
