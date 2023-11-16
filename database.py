import pymysql

# 数据库连接配置
host = '127.0.0.1'  # 例如 'localhost' 或 '127.0.0.1'
port = 3306  # 数据库端口
user = 'root'  # 您的数据库用户名
password = 'zxcvbnm123'  # 您的数据库密码
db = 'faculty'  # 您要连接的数据库名

# 创建数据库连接
connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db)


# CREATE TABLE department (
#     department_id INT AUTO_INCREMENT PRIMARY KEY,
#     department_name VARCHAR(100),
#     manager_id INT
# );
#
# CREATE TABLE staff (
#     staff_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     gender VARCHAR(10),
#     birth_date DATE,
#     title VARCHAR(50),
#     department_id INT,
#     FOREIGN KEY (department_id) REFERENCES department(department_id)
# );
#
# CREATE TABLE course (
#     course_id INT AUTO_INCREMENT PRIMARY KEY,
#     course_name VARCHAR(100),
#     credits INT
# );
#
# CREATE TABLE teach (
#     staff_id INT,
#     course_id INT,
#     semester VARCHAR(20),
#     PRIMARY KEY (staff_id, course_id, semester),
#     FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
#     FOREIGN KEY (course_id) REFERENCES course(course_id)
# );
#
# CREATE TABLE education (
#     education_id INT AUTO_INCREMENT PRIMARY KEY,
#     staff_id INT,
#     degree VARCHAR(50),
#     major VARCHAR(100),
#     university VARCHAR(100),
#     graduation_year YEAR,
#     FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
# );
#
# CREATE TABLE salary (
#     salary_id INT AUTO_INCREMENT PRIMARY KEY,
#     staff_id INT,
#     amount DECIMAL(10, 2),
#     pay_date DATE,
#     FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
# );
#
# CREATE TABLE project (
#     project_id INT AUTO_INCREMENT PRIMARY KEY,
#     project_name VARCHAR(100),
#     start_date DATE,
#     end_date DATE
# );
#
# CREATE TABLE participate (
#     project_id INT,
#     staff_id INT,
#     role VARCHAR(50),
#     join_date DATE,
#     PRIMARY KEY (project_id, staff_id),
#     FOREIGN KEY (project_id) REFERENCES project(project_id),
#     FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
# );


# staff部分

# 获取所有员工信息
def getAllStaff():
    try:
        # 创建 cursor 对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT * FROM `staff`"
            cursor.execute(sql)
            # 获取查询结果
            results = cursor.fetchall()
            print(results)
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 添加员工信息
def addStaff(name, gender, birth_date, title, department_id):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 插入语句
            sql = "INSERT INTO `staff` (`name`, `gender`, `birth_date`, `title`, `department_id`) VALUES (%s, %s, %s, %s, %s)"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, (name, gender, birth_date, title, department_id))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


def deleteStaff(staff_id):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 删除语句
            sql = "DELETE FROM `staff` WHERE `staff_id`=%s"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, staff_id)
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 修改员工信息
def updateStaff(staff_id, name, gender, birth_date, title, department_id):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `staff` SET `name`=%s,`gender`=%s,`birth_date`=%s,`title`=%s,`department_id`=%s WHERE `staff_id`=%s"
            cursor.execute(sql, (name, gender, birth_date, title, department_id, staff_id))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


def getStaff(staff_id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `staff` WHERE `staff_id`=%s"
            cursor.execute(sql, staff_id)
            results = cursor.fetchall()
            print(results)
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 查询对应的员工
def selectStaff(staff_id, name, gender, birth_date, title, department_id):
    try:
        with connection.cursor() as cursor:
            # 使用参数化查询
            sql = '''
            SELECT * FROM `staff`
            WHERE (%s IS NULL OR staff_id = %s)
            AND (%s IS NULL OR name = %s)
            AND (%s IS NULL OR gender = %s)
            AND (%s IS NULL OR birth_date = %s)
            AND (%s IS NULL OR title = %s)
            AND (%s IS NULL OR department_id = %s)
            '''
            cursor.execute(sql, (staff_id, staff_id, name, name, gender, gender, birth_date, birth_date, title, title, department_id, department_id))
            results = cursor.fetchall()
            print(results)
    except  Exception as e:
        print("发生错误：", e)
        connection.rollback()



selectStaff(None, None, "男", None, None, None)