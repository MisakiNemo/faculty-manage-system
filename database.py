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
            cursor.execute(sql, (
            staff_id, staff_id, name, name, gender, gender, birth_date, birth_date, title, title, department_id,
            department_id))
            results = cursor.fetchall()
            print(results)
    except  Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 课程部分
# 获取所有课程信息
def getAllCourse():
    try:
        # 创建 cursor 对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT * FROM `course`"
            cursor.execute(sql)
            # 获取查询结果
            results = cursor.fetchall()
            print(results)
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 添加课程信息
def addCourse(course_name, credits):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 插入语句
            sql = "INSERT INTO `course` (`course_name`, `credits`) VALUES (%s, %s)"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, (course_name, credits))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 删除课程信息
def deleteCourse(course_id):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 删除语句
            sql = "DELETE FROM `course` WHERE `course_id`=%s"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, course_id)
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 修改课程信息
def updateCourse(course_id, course_name, credits):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `course` SET `course_name`=%s,`credits`=%s WHERE `course_id`=%s"

            cursor.execute(sql, (course_name, credits, course_id))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 查询对应的课程
def selectCourse(course_id, course_name, credits):
    try:
        with connection.cursor() as cursor:
            # 使用参数化查询
            sql = '''
            SELECT * FROM `course`
            WHERE (%s IS NULL OR course_id = %s)
            AND (%s IS NULL OR course_name = %s)
            AND (%s IS NULL OR credits = %s)
            '''
            cursor.execute(sql, (course_id, course_id, course_name, course_name, credits, credits))
            results = cursor.fetchall()
            print(results)
    except  Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 部门部分
# 获取所有部门信息
def getAllDepartment():
    try:
        # 创建 cursor 对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT * FROM `department`"
            cursor.execute(sql)
            # 获取查询结果
            results = cursor.fetchall()
            print(results)
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 添加部门信息
def addDepartment(department_name, manager_id):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 插入语句
            sql = "INSERT INTO `department` (`department_name`, `manager_id`) VALUES (%s, %s)"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, (department_name, manager_id))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 删除部门信息
def deleteDepartment(department_id):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 删除语句
            sql = "DELETE FROM `department` WHERE `department_id`=%s"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, department_id)
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 修改部门信息
def updateDepartment(department_id, department_name, manager_id):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `department` SET `department_name`=%s,`manager_id`=%s WHERE `department_id`=%s"

            cursor.execute(sql, (department_name, manager_id, department_id))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 查询对应的部门
def selectDepartment(department_id, department_name, manager_id):
    try:
        with connection.cursor() as cursor:
            # 使用参数化查询
            sql = '''
            SELECT * FROM `department`
            WHERE (%s IS NULL OR department_id = %s)
            AND (%s IS NULL OR department_name = %s)
            AND (%s IS NULL OR manager_id = %s)
            '''
            cursor.execute(sql,
                           (department_id, department_id, department_name, department_name, manager_id, manager_id))
            results = cursor.fetchall()
            print(results)
    except  Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 工资部分
# 获取所有工资信息
def getAllSalary():
    try:
        # 创建 cursor 对象
        with connection.cursor() as cursor:
            # 执行 SQL 查询
            sql = "SELECT * FROM `salary`"
            cursor.execute(sql)
            # 获取查询结果
            results = cursor.fetchall()
            print(results)
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 添加工资信息
def addSalary(staff_id, amount, pay_date):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 插入语句
            sql = "INSERT INTO `salary` (`staff_id`, `amount`, `pay_date`) VALUES (%s, %s, %s)"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, (staff_id, amount, pay_date))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 删除工资信息
def deleteSalary(salary_id):
    try:
        with connection.cursor() as cursor:
            # 正确的 SQL 删除语句
            sql = "DELETE FROM `salary` WHERE `salary_id`=%s"
            # 执行 SQL 语句并传递参数
            cursor.execute(sql, salary_id)
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 修改工资信息
def updateSalary(salary_id, staff_id, amount, pay_date):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `salary` SET `staff_id`=%s,`amount`=%s,`pay_date`=%s WHERE `salary_id`=%s"

            cursor.execute(sql, (staff_id, amount, pay_date, salary_id))
            connection.commit()
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


# 用户登录
def login(username, password) -> bool:
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `username`=%s AND `password`=%s"
            cursor.execute(sql, (username, password))
            results = cursor.fetchall()
            print(results)
            if len(results) == 0:
                return False
            else:
                return True
    except Exception as e:
        print("发生错误：", e)
        connection.rollback()


