<<<<<<< HEAD
import json 

def sortById(e):
    return e['id']


 def assignment2():
    with open('ex5.json', 'r') as jsonFile:
        if not jsonFile.readline():
            print('file is empty')
            return
        jsonFile.seek(0)
        ex5 = json.load(jsonFile)
        jsonFile.close()

    for data in ex5:
        if (type(data) is not dict):
            print('Data is not in the type of dict')
            return
        if'Old Fashioned' in data['name'] and 'donut' in data['type']:
           batters = data['batters']['batter']
           if any('Coffee' in batter['type'] for batter in batters):
              print('Type Coffee already present in the batter')
              return
           batters.sort(key=sortById)
           newid = int(batters[-1]['id'])+1
           batters.append({'id': str(newid), 'type': 'Coffee'})
           print(f"Added batter type Coffee with new id {newId}.")

    with open('ex5.json', 'w') as jsonFile:
        json.dump(ex5, jsonFile)
        jsonFile.close()


=======
import json 

def sortById(e):
    return e['id']


 def assignment2():
    with open('ex5.json', 'r') as jsonFile:
        if not jsonFile.readline():
            print('file is empty')
            return
        jsonFile.seek(0)
        ex5 = json.load(jsonFile)
        jsonFile.close()

    for data in ex5:
        if (type(data) is not dict):
            print('Data is not in the type of dict')
            return
        if'Old Fashioned' in data['name'] and 'donut' in data['type']:
           batters = data['batters']['batter']
           if any('Coffee' in batter['type'] for batter in batters):
              print('Type Coffee already present in the batter')
              return
           batters.sort(key=sortById)
           newid = int(batters[-1]['id'])+1
           batters.append({'id': str(newid), 'type': 'Coffee'})
           print(f"Added batter type Coffee with new id {newId}.")

    with open('ex5.json', 'w') as jsonFile:
        json.dump(ex5, jsonFile)
        jsonFile.close()


>>>>>>> 008c48c5ad34b63e8ad9f80d092161c7a9147215
 assignment2()                       