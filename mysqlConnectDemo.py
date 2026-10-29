import mysql.connector

con_obj = mysql.connector.connect(host="localhost",user="root",passwd="root",database="mysql_demo")

print("Conected to mysql_demo database....")

cursor_obj = con_obj.cursor()

# cursor_obj.execute("show databases")

# for database in cursor_obj:
#     print(database)

# CRUD Operations - > Create ,Read , Update , Delete
# Create the student table

# query = "CREATE TABLE student (id int auto_increment primary key , name varchar(64),age int) "

# query = "INSERT INTO student (name,age) VALUES ('Bharath',25)"
# query = "SELECT * from student where age=23"
query = "UPDATE student SET age=31 WHERE id = 1"
cursor_obj.execute(query)
con_obj.commit()

sele_query = "SELECT * FROM student"
cursor_obj.execute(sele_query)
for student in cursor_obj:
    print(student)

del_query = "DELETE FROM student where age=25"
cursor_obj.execute(del_query)
con_obj.commit()

sele_query = "SELECT * FROM student"
cursor_obj.execute(sele_query)
for student in cursor_obj:
    print(student)

# print("Student table data added successfully...")
