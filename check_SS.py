import SQLEasy
DB = SQLEasy.database('database.db')
data = DB.getBase('langs')[0]
for key in data:
    if data[key] == 'saw table':
        print(key)
input()