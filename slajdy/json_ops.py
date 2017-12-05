import json

with open('MOCK_DATA.json') as f:
    print(json.read(f))

with open('new_data.json', 'w') as f:
    json.dump({'name': 'Jon', 'surname': 'Snow'})

