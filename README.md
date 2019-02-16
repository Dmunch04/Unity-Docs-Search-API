# Unity-Docs-Search-API
Search the Unity Docs (Manual and Script)

Example of use:
```python
  import docssearcher as ds
  
  def mySearch (search, docs):
    result = search("2D", "script")    # Calls the search function and tells it to search for 2D in the Script Docs

    print(result.title)                # Prints the title of the result page
    print(result.description)          # Prints the description of the result page
    print(result.url)                  # Prints the link of the result page
```
