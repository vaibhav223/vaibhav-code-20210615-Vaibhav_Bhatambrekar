import pymysql
import json
import create_table


def calculateBmi(inputdata):

    try:

        # loop to parse json data
        cursor, connection = create_table.db_Connection()
        resp = {}
        for data in inputdata:
            gender = data["Gender"]
            height = data["HeightCm"]
            mass = data["WeightKg"]
            bmi_Category = ""
            health_Risk = ""
            counter = 0
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
                counter = counter+1

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

                count = calculate_Overweight_person(cursor, connection)
                resp["Code"] = 200
                resp["Msg"] = "Success"
                resp["Overweight Person Count for input"] = counter
                resp["Overweight Person Total Count in table"] = count
            except pymysql.Error as sqlerror:
                print("sql error", sqlerror)
                resp["Code"] = 510
                resp["Msg"] = "Exception in sql try catch"

        return resp
    except Exception as Identifier:
        print(Identifier)
        resp["Code"] = 512
        resp["Msg"] = "Exception in main try catch"
        return resp


def calculate_Overweight_person(cursor, connection):
    try:
        sqlQuery = "SELECT COUNT(1) FROM BMI_DATA WHERE PERSON_BMI_CATEGORY='Overweight';"
        cursor.execute(sqlQuery)
        result_data = cursor.fetchall()

        for data in result_data:
            count = data[0]
        return count
    except pymysql.Error as sqlerror:
        count = -1
        return count


if __name__ == "__main__":

    fp = open('inputdata.json',)
    inputdata = json.load(fp)
    calculateBmi(inputdata)
