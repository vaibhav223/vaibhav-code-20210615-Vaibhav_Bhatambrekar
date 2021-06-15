import pymysql
import json


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


def calculateBmi(inputdata):

    # loop to parse json data
    cursor, connection = db_Connection()
    for data in inputdata:
        gender = data["Gender"]
        height = data["HeightCm"]
        mass = data["WeightKg"]
        bmi_Category = ""
        health_Risk = ""
        # below variable to convert height into meters
        heightm = round(0.01*data["HeightCm"], 2)
        bmi = round(float(mass/(heightm*heightm)), 3)

        if bmi <= 18.4 and bmi > 0:
            bmi_Category = "Underweight"
            health_Risk = "Malnutrition risk"

        elif bmi < 25 and bmi >= 18.5:
            bmi_Category = "Normal weight"
            health_Risk = "Low risk"

        elif bmi < 30 and bmi >= 25:
            bmi_Category = "Overweight"
            health_Risk = "Enhanced risk"

        elif bmi < 35 and bmi >= 30:
            bmi_Category = "Moderately obese"
            health_Risk = "Medium risk"

        elif bmi < 40 and bmi >= 35:
            bmi_Category = "Severely obese"
            health_Risk = "High risk"

        elif bmi < 54 and bmi >= 40:
            bmi_Category = "Very severely obese"
            health_Risk = "Very high risk"
        else:
            bmi_Category = "Unknown"
            health_Risk = "Unknown"
        try:
            sql_Insert_Data = "INSERT INTO BMI_DATA (PERSON_GENDER,PERSON_HEIGHT,PERSON_WEIGHT,PERSON_BMI,PERSON_BMI_CATEGORY,PERSON_HEALTH_RISK) VALUES(%s,%s,%s,%s,%s,%s);"
            values = [gender, height, mass, bmi, bmi_Category, health_Risk]
            cursor.execute(sql_Insert_Data, values)
            connection.commit()

        except Exception as Identifier:
            print(Identifier)
    return 'expected_output'


if __name__ == "__main__":

    fp = open('inputdata.json',)
    inputdata = json.load(fp)
    calculateBmi(inputdata)
