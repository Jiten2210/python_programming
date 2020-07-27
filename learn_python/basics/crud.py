"""crud module"""

import pymysql.cursors


def connection():
    SERVER_URL = "localhost"
    DB = "test_db"
    USER_NAME = "root"
    PASSWORD = "jitu1234"

    DB_CONNECTION = pymysql.connect(host=SERVER_URL,
                                    user=USER_NAME,
                                    passwd=PASSWORD,
                                    db=DB,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)

    return DB_CONNECTION


def close_connection(DB_CONNECTION):

    DB_CONNECTION.close()


def create_record():

    DB_CONNECTION = connection()

    SQL = "INSERT INTO test_db.cars(car_model, car_brand) VALUES ('accord', 'honda')"

    with DB_CONNECTION.cursor() as cursor:
        try:
            sql_exec = cursor.execute(SQL)
            if sql_exec:
                print(sql_exec)
                print("Record Added")
            else:
                print(sql_exec)
                print("Not Added")
        except (pymysql.Error, pymysql.Warning) as e:
            print('error! {e}')

        finally:
            close_connection(DB_CONNECTION)


def read_record():

    DB_CONNECTION = connection()

    SQL = "SELECT * FROM test_db.cars"

    with DB_CONNECTION.cursor() as cursor:
        try:
            sql_exec = cursor.execute(SQL)
            if sql_exec:
                print(sql_exec)
                print(cursor.fetchall())
            else:
                print(sql_exec)
                print("No Record")
        except (pymysql.Error, pymysql.Warning) as e:
            print('error! {e}')

        finally:
            close_connection(DB_CONNECTION)


def update_record():
    DB_CONNECTION = connection()

    SQL = "UPDATE test_db.cars SET car_model = 'explorer', car_brand = 'ford' WHERE id = '1'"

    with DB_CONNECTION.cursor() as cursor:
        try:
            sql_exec = cursor.execute(SQL)
            if sql_exec:
                print(sql_exec)
                print("Record Upadted")
            else:
                print(sql_exec)
                print("Not Upadted")
        except (pymysql.Error, pymysql.Warning) as e:
            print('error! {e}')

        finally:
            close_connection(DB_CONNECTION)


def delete_record():

    DB_CONNECTION = connection()

    SQL = "DELETE FROM test_db.cars WHERE id = '1'"

    with DB_CONNECTION.cursor() as cursor:
        try:
            sql_exec = cursor.execute(SQL)
            if sql_exec:
                print(sql_exec)
                print("Record Deleted")
            else:
                print(sql_exec)
                print("Not Deleted")
        except (pymysql.Error, pymysql.Warning) as e:
            print('error! {e}')

        finally:
            close_connection(DB_CONNECTION)

#create_record()
#update_record()
read_record()
delete_record()
read_record()