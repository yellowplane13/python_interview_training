import requests #to make TMDB API calls

# #Discover API url filtered to movies >= 2004 and containing Drama genre_ID: 18
# discover_api_url = 'https://api.themoviedb.org/3/discover/movie? 
# api_key=['my api key']&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=>%3D2004&with_genres=18'

# discover_api = requests.get(discover_api_url).json()
# most_popular_films = discover_api["results"]
# for page in range(2, discover_api["total_pages"]+1):
#     discover_api = requests.get(discover_api_url + f"&page={page}").json()
#     most_popular_films.extend(discover_api["results"])

#printing movie_id and movie_title by popularity desc
# for i, film in enumerate(most_popular_films):
#     print(i, film['id'], film['title'])

countries_url = "https://jsonmock.hackerrank.com/api/countries/search?name=co"
countries_api = requests.get(countries_url).json()

most_populated_countries = {}
c = 0
for page in range(1,countries_api['total_pages']+1):
    countries_api = requests.get(countries_url + f"&page={page}").json()
    #most_popular_films.extend(discover_api["results"])
    print("page:",page)
    for country in countries_api['data']:
        if country['population'] > 500:
            print("country:",country['name'])
            c+=1
            most_populated_countries[country['name']] = country['population']


print(most_populated_countries)
print(c)