import sys
import json

class DocsResult (object):
  def __init__ (self, title, description, url):
    self.title = title
    self.description = description
    self.url = url

  def __str__ (self):
    return '%s: %s (%d)' % (self.title, self.description, self.url)

def get_search_json (docs):
  rawData = open('UnityDocs.' + docs + '.json')

  jsonData = json.load(rawData)

  return jsonData

def parse_search_json (searchItem, json):
  results = []

  for element in json:
    if searchItem in element['title']:
      result = DocsResult(str(element['title']), str(element['description']), str(element['link']))
      results.append(result)

  # Check for the result closest to the searchItem instead here
  return results[0]

def search (search, docs):
  json = get_search_json (docs)
  return parse_search_json (search, json)
