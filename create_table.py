import bmi_Calculator
import pymysql


def db_Connection():
    try:
        # Database credential initialization
        endpoint = "localhost"
        username = "root"
        password = "admin"
        database_name = "bmicalc"

        # Connection to database
        connection = pymysql.connect(
            host=endpoint, user=username, passwd=password, db=database_name)
        cursor = connection.cursor()
        return cursor, connection
    except Exception as Identifier:
        print(Identifier)


def createtable():
    resp = {}
    try:

        cursor, connection = db_Connection()
        sqlCreateTable = """CREATE TABLE IF NOT EXISTS bmi_data (
                        BMI_DATA_ID int NOT NULL AUTO_INCREMENT,
                        PERSON_GENDER varchar(50) NOT NULL,
                        PERSON_HEIGHT varchar(50) NOT NULL,
                        PERSON_WEIGHT varchar(50) NOT NULL,
                        PERSON_BMI varchar(50) NOT NULL,
                        PERSON_BMI_CATEGORY varchar(50) NOT NULL,
                        PERSON_HEALTH_RISK varchar(50) NOT NULL,
                        BMI_DATA_TS timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        PRIMARY KEY (BMI_DATA_ID)
                        );
                        """
        cursor.execute(sqlCreateTable)
        connection.commit()
        resp["Msg"] = "Table Created Successfully"
        return resp
    except pymysql.Error as sqlerror:
        resp["Msg"] = "Error in table Creation"
        return resp


if __name__ == "__main__":

    result = createtable()
    print(result)
