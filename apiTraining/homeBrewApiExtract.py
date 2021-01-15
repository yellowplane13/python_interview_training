import requests
import json
import time

name = {}
desc = {}
r = requests.get('https://formulae.brew.sh/api/formula.json')
#print(r.status_code)
packagesJson = r.json()
#print(len(packagesJson))
#prints out the package name from the list of packages
packageName = packagesJson[0]['name']
results = []
time1 = time.perf_counter()
for package in packagesJson:
    name = package["name"]
    desc = package["desc"]
    apiUrl = f"https://formulae.brew.sh/api/formula/{name}.json"
    r = requests.get(apiUrl)
    opJson = r.json()
    install_30d = opJson['analytics']['install_on_request']['30d'][name]
    install_60d = opJson['analytics']['install_on_request']['90d'][name]
    install_365d = opJson['analytics']['install_on_request']['365d'][name]
    data = {
        'name': name,
        'desc': desc,
        '_analytics': {
            '30d': install_30d,
            '60d': install_60d,
            '365d': install_365d,
        }
    }
    results.append(data)
    time.sleep(r.elapsed.total_seconds())
    print(f"got {name} in {r.elapsed.total_seconds()} seconds")

time2 = time.perf_counter()
print(f"finished in {time2-time1} seconds")
with open('package_info.json', 'w') as f:
    json.dump(results,f,indent=4)

#print(name, desc, install_30d, install_60d, install_365d)
#print(results)


#print(packageName)


# take the name from the previous json file and add it as an end point to the api call for individual packages
# packageApiUrl = f'https://formulae.brew.sh/api/formula/{packageName}.json'
# p  = requests.get(packageApiUrl)
# packageJson = p.json()
# packageStr = json.dumps(packageJson, indent=4)
# install_30d = packageJson['analytics']['install_on_request']['30d'][packageName]
# install_60d = packageJson['analytics']['install_on_request']['90d'][packageName]
# install_60d = packageJson['analytics']['install_on_request']['365d'][packageName]
