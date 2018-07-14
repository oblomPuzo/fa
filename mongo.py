import pymongo
input_email = open ('input.txt','r')
email_num = 0
count=1
user_email = input_email.readline()
for line in input_email:
    count+=1
while email_num < count:
    input_email = open('input.txt', 'r')
    user_email = input_email.readlines()[email_num][:-5]
    uri = "mongodb://127.0.0.1:27017"
    client = pymongo.MongoClient(uri)
    db = client['test']
    users = db ['users']
    find_users_id = users.find_one ({"email":user_email},{'_id':0,'remote_id':1})
    users_id = (str(find_users_id))
    exact_id = "remote_id':{} "
    for char in exact_id:
        users_id = users_id.replace(char, "")
    if find_users_id == None:
        o = open("output.txt", 'a')
        o.write('0.0 ')
        email_num+=1
        continue
    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb
    conn = MySQLdb.connect(host='localhost',database='Mysql',user='root',password='root')
    cursor = conn.cursor()
    cursor.execute(" select balance  FROM test.users where user_id = %s", users_id)
    if cursor.execute ==0:
        o = open("output.txt", 'a')
        o.write('0.0 ')
        email_num += 1
        continue
    find_balance =cursor.fetchone()
    balance = (str(find_balance))
    exact_balance = "(), "
    for char in exact_balance:
        balance = balance.replace (char,"")
    o = open('output.txt','a')
    o.write (str(balance )+" ")
    conn.close()
    email_num+=1




