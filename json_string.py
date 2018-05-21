import json
people_string ='''
{
    "people": [
        {
            "name": "preeti",
            "phone": "408-707-0669",
            "has_license": false
        },

        {
            
            "name": "viaan",
            "phone": "408-802-4329",
            "has_license": true

        }
    ]
}
'''
data=json.loads(people_string)
print(data)
print (type(data['people']))

for person in data['people']:
    del person['phone']

new_string=json.dumps(data,indent=2,sort_keys=True)
print new_string
