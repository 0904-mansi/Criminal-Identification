import pymysql

def insertData(data):
    print(data)
    rowId = 0

    # To connect MySQL database
    db = pymysql.connect(
        host='localhost',
        user='root', 
        password = "",
        db='criminaldb2',
        )
      
    cursor = db.cursor()
    print("database connected")

    query = "INSERT INTO missingdata VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Report-ID"], data["Name"], data["Father's Name"], data["Address"],
             data["Phone"], data["Gender"], data["DOB(yyyy-mm-dd)"],
             data["Identification"], data["Date of Missing(yyyy-mm-dd)"], data["Place of Missing"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")


    db.close()
    print("connection closed")
    return rowId

def retrieveData(name):
    id = None
    crim_data = None

    db = pymysql.connect(
        host='localhost',
        user='root', 
        password = "",
        db='criminaldb',
        )
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM criminaldata WHERE name='%s'"%name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id=result[0]
        crim_data = {
            "Name" : result[1],
            "Father's Name" : result[2],
            "Address":result[3],
            "Phone":result[4],
            "Gender" : result[5],
            "DOB(yyyy-mm-dd)" : result[6],
            "Identification" : result[7],
            "Date of Missing(yyyy-mm-dd)":result[8],

            "Place of Missing" : result[9]
        }

        print("data retrieved")
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, crim_data)
