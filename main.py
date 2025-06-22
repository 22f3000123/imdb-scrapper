import requests

# fetch IMDB top 250 movies
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)

# save it in a file
with open('top-movies.html', 'wb') as file:
    file.write(response.content)
