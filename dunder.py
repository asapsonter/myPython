# todos = open('todos.txt', 'a')
# print('Put out the trash.', file=todos)
# print('Feed the cat.', file=todos)
# print('Prepare tax return.', file=todos)      

# task = open('todos.txt')
# for chore in task:
#     print(chore)
# task.close()    

dbconfig = {
    'host': '127.0.0.1',
    'user':  ' vsearch',
    'password' : 'vsearchpasswd',
    'database': 'vsearchlogDB',
}

import mysql.connector 
# set val to pass db dict to python mysql connector 
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor() #cursor sends command to server and also receives results
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
(%s, %s, %s, %s, %s)""" # assign query to a val 
cursor.execute(_SQL, ('galaxy', 'xyz', '127.0.0.1', 'Opera', "{'x', 'y'}")) # send the query for execution
conn.commit()

_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

cursor.close()   
conn.close() 
