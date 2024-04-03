import mysql.connector

if __name__ == '__main__':

    mydb = mysql.connector.connect(

        host = '172.17.0.4',
        user = 'test0',
        password = 'test0',
        database = 'python_project'

    )

    mycursor = mydb.cursor()

    error: str = ""

    #sql: str = "INSERT INTO users(login,password) VALUES(%s, %s)"
    #val: tuple = ("root","ZAQ!2wsx")

    #mycursor.execute(sql,val)

    sql: str = "SELECT u.id,u.login,u.password FROM users AS u WHERE u.id = %s"
    adr: tuple = ("5", )

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()

    for res in myresult:
        print(res)

    #mydb.commit()

    print(mycursor.rowcount)

    for x in mycursor:
        print(x)