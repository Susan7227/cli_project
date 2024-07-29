import sqlite3


def create_connection():
    try:
        con = sqlite3.connect("users.sqlite3")
        return con
    except Exception as e:
        print(e)


INPUT_STRINMG = """
ENter the option:
1. Create table
2. DUMP user from csv INTO users table
3. add new user into users table
4. query all users from table
5. query user ny id from table
6. query specified no. of records from table
7. delete users
8. delet user by id
9. update user
10. press any key to exit
"""

def create_table(con):
    CREATE_USERS_TABLE_QUERY="""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR (255) NOT NULL,
            last_name CHAR (255) NOT NULL,
            company_name CHAR (255) NOT NULL,
            address CHAR (255) NOT NULL,
            city CHAR (255) NOT NULL,
            county CHAR (255) NOT NULL,
            state CHAR (255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR (255) NOT NULL,
            phone2 CHAR (255) NOT NULL,
            email CHAR (255) NOT NULL,
            web text
        );
    """
    cur=con.cursor()
    cur.execute (CREATE_USERS_TABLE_QUERY)
    print("Successfully created in the table.")

import csv


def read_csv():
    users = []
    with open ("sample_users.csv", "r") as f:
        data = csv.reader(f)
        for user in data:
            users.append(tuple(user))
    return users[1:]

def insert_users(con, users):
    user_add_query = """
        INSERT INTO users
        (
            first_name,
            last_name,
            company_name,
            address,
            city,
            county,
            state,
            zip,
            phone1,
            phone2,
            email,
            web
        )
        values(?,?,?,?,?,?,?,?,?,?,?,?);
    """
    cur = con.cursor()
    cur.executemany(user_add_query, users)
    con.commit()
    print(f"{len(users)} users were import successfully.")

def select_users(con,no_of_users=0):
    cur=con.cursor()
    users=cur.execute("SELECT * FROM users ;")
    for i, user in enumerate(users):
        if no_of_users and  no_of_users==i:
            break
        print(user)



def select_user_by_id(con,user_id):
    cur = con.cursor()
    users = con.execute("select * from users where id = ?;",(user_id))
    for user in users:
        print(user)

def delete_users(con):
    cur = con.cursor()
    cur.execute("delete from users;")
    con.commit
    print("all users are deleted successfully.")

def delete_user_by_id(con, user_id):
    cur = con.cursor()
    cur.execute ("delete from users where id = ?", (user_id,))
    con.commit()
    print(f"user with id [{user_id}] was successfully deleted.")


columns = (
    "first_name",
    "last_name",
    "company_name",
    "address",
    "city",
    "country",
    "state",
    "zip",
    "phone1",
    "phone2",
    "email",
    "web",
)
#CURD => Create , Read , Update , Delete
#git config --global user.name "Susan Nagarkoti"
#git config --global user.email "sushanu2017@gmail.com"
#git init

#git add .
# git commit -m "commit message"
#git push origin


def main():
    con =  create_connection()
    user_input = input(INPUT_STRINMG)
    if user_input == "1":
        create_table(con)

    elif user_input == "2":
        users = read_csv()
        insert_users(con, users)

    elif user_input == "3":
        input_data =[]
        for c in columns:
            column_value = input(f"Enter the value of {c}:")
            input_data.append(column_value)
        users = [tuple(input_data)]
        insert_users(con, users)
    
    elif user_input == "4":
        select_users(con)

    elif user_input == "5":
        user_id = input("enter the id of uder:")
        if user_id.isnumeric():
            select_user_by_id(con, user_id)

    elif user_input == "6":
        no_of_users = input( "enter the number of user to fetch:")
        if no_of_users.isnumeric() and int (no_of_users)> 0:
            select_users(con, no_of_users =int(no_of_users))
    
    elif user_input == "7":
        confirmation = input("are you sure  you wannt yo delete all users? (y,n)")
        if confirmation == "y":
            delete_users(con)


    elif user_input == "8":
        user_id = input("enter id of user: ")
        if user_id.isnumeric():
            delete_user_by_id(con,user_id)

    elif user_input == "9":
        user_id = input("enter id of user")
        if user_id.isnumeric():
            column_name= input(
                f"enter the column you wamt to edit.please make sure colums is with in{columns}:"
            )
            if column_name in columns:
                column_value= input(f"enter the value of column {column_name}:")
                update_user_by_id(con,user_id,column_name,column_value)

    else:
        exit()


def update_user_by_id(con,user_id,column_name,column_value):
    update_query= f"update user set {column_name}= ? where is =?;"
    cur= con.cursor()
    cur.execute(update_query,(column_value,user_id))
    con.commit()
    print(
        f"[{column_name}] was update with value [{column_value}] of user with id [{user_id}]"
    )

main()

#test git


