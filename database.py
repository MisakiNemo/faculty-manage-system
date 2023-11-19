import pymysql

# 数据库连接配置
host = '127.0.0.1'  # 例如 'localhost' 或 '127.0.0.1'
port = 3306  # 数据库端口
user = 'root'  # 您的数据库用户名
password = 'zxcvbnm123'  # 您的数据库密码
db = 'faculty'  # 连接的数据库名

# 创建数据库连接
connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db)


# create table course
# (
#     course_id   int auto_increment
#         primary key,
#     course_name varchar(100) null
# );
#
# create table department
# (
#     department_id   int auto_increment
#         primary key,
#     department_name varchar(100) null
# );
#
# create table staff
# (
#     staff_id      int auto_increment
#         primary key,
#     name          varchar(100) null,
#     gender        varchar(10)  null,
#     birth_date    date         null,
#     department_id int          null,
#     constraint staff_ibfk_1
#         foreign key (department_id) references department (department_id)
# );
#
# create table salary
# (
#     salary_id int auto_increment
#         primary key,
#     staff_id  int            null,
#     amount    decimal(10, 2) null,
#     pay_date  date           null,
#     constraint salary_ibfk_1
#         foreign key (staff_id) references staff (staff_id)
# );
#
# create index staff_id
#     on salary (staff_id);
#
# create index department_id
#     on staff (department_id);
#
# create table user
# (
#     user_id  int auto_increment
#         primary key,
#     username varchar(50) null,
#     password varchar(50) null
# );


# staff部分

# 获取所有员工的信息，并且返回一个列表，员工的部门id改为部门名称，并且返薪水的多少
def getAllStaffs():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT staff.staff_id, staff.name, staff.gender, staff.birth_date, department.department_name, salary.amount FROM staff INNER JOIN department ON staff.department_id = department.department_id LEFT JOIN salary ON staff.staff_id = salary.staff_id ORDER BY staff.staff_id ASC"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except:
        print("Error: get all staffs failed")


# 根据员工id删除员工
def deleteStaff(staff_id):
    try:
        with connection.cursor() as cursor:
            # 删除该员工的薪资记录
            sql = "DELETE FROM salary WHERE staff_id = %s"
            cursor.execute(sql, (staff_id,))
            connection.commit()
            sql = "DELETE FROM staff WHERE staff_id = %s"
            cursor.execute(sql, (staff_id,))
            connection.commit()

    except:
        print("Error: unable to delete data")


# 修改员工信息
def updateStaff(staff_id, name, gender, birth_date, department_name, salary):
    print(staff_id, name, gender, birth_date, department_name, salary)
    try:
        with connection.cursor() as cursor:
            department_id = getDepartmentByName(department_name)[0]
            sql = "UPDATE staff SET name = %s, gender = %s, birth_date = %s, department_id = %s WHERE staff_id = %s"
            cursor.execute(sql, (name, gender, birth_date, department_id, staff_id))
            connection.commit()
            sql = "UPDATE salary SET amount = %s WHERE staff_id = %s"
            cursor.execute(sql, (salary, staff_id))
            connection.commit()
    except:
        print("Error: unable to update data")


def getAllDepartMents():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM department"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print("Error: unable to fetch data")


def getDepartmentByName(department_name):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM department WHERE department_name = %s"
            cursor.execute(sql, (department_name,))
            result = cursor.fetchone()
            return result
    except Exception as e:
        print("Error: unable to fetch data")
    finally:
        print("Error: unable to fetch data")


def addStaff(name, gender, birth_date, department_name, salary):
    if salary == '':
        salary = 0
    try:
        with connection.cursor() as cursor:
            # 获取部门 ID
            department_id = None
            cursor.execute("SELECT department_id FROM department WHERE department_name = %s", (department_name,))
            result = cursor.fetchone()
            if result:
                department_id = result[0]

            # 插入员工信息到 staff 表
            sql_staff = "INSERT INTO staff (name, gender, birth_date, department_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_staff, (name, gender, birth_date, department_id))
            connection.commit()

            # 获取插入的员工的 staff_id
            staff_id = cursor.lastrowid

            # 插入工资信息到 salary 表
            sql_salary = "INSERT INTO salary (staff_id, amount, pay_date) VALUES (%s, %s, NOW())"
            cursor.execute(sql_salary, (staff_id, salary))
            connection.commit()

    except Exception as e:
        print("发生异常:", e)


def getStaffByName(name):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT staff.staff_id, staff.name, staff.gender, staff.birth_date, department.department_name, salary.amount FROM staff   INNER JOIN department ON staff.department_id = department.department_id LEFT JOIN salary ON staff.staff_id = salary.staff_id WHERE name=%s ORDER BY staff.staff_id ASC"
            cursor.execute(sql, (name,))
            result = cursor.fetchall()
            return result
    except Exception as e:
        print("Error: get staff by name failed")


def getStaffByID(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT staff.staff_id, staff.name, staff.gender, staff.birth_date, department.department_name, salary.amount FROM staff   INNER JOIN department ON staff.department_id = department.department_id LEFT JOIN salary ON staff.staff_id = salary.staff_id WHERE staff.staff_id=%s ORDER BY staff.staff_id ASC"
            cursor.execute(sql, (id,))
            result = cursor.fetchall()
            return result
    except Exception as e:
        print("Error: unable to fetch data")


def login(username, password):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            return True if result else False
    except Exception as e:
        print("Error: unable to fetch data")
