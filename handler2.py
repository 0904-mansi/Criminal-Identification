import csv
import pymysql
# filename = "Criminal_count.csv"
# num=0
# with open(filename, 'w') as csvfile: 
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow([5])


def insertData(data):
    field = ["Criminal-ID", "Address", "Phone", "Name", "Father's Name",
    "Gender", "DOB(yyyy-mm-dd)", "Crimes Done", "Date of Arrest(yyyy-mm-dd)",
    "Place of Arrest"]
    x = [data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'],
     data['Crimes Done'], data['Date of Arrest(yyyy-mm-dd)'], data["Place of Arrest"] ]
    filen = "Criminal.csv"
    with open(filen, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerow(x)

def insertData(data):
    print(data['Name'])
    print(data['Report-ID'])
    rowId = 0
    db = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
    cursor = db.cursor()
    print("Opened Database")
    print("Database Connected successfully")
    query = "INSERT INTO missingdata VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Report-ID"], data["Name"], data["Father's Name"], data["Address"],
             data["Phone"], data["Gender"], data["DOB(yyyy-mm-dd)"],
             data["Identification"], data["Date of Missing(yyyy-mm-dd)"], data["Place of Missing"])

    cursor.execute(query)
    db.commit()
    rowId = cursor.lastrowid
    # print("RowId %d" % rowId)
    print("data stored on new row in the database")



    print("Record Created")
    db.close()
    return rowId


# def insertData(data):
#     field = ["Report-ID", "Name", "Phone", "Father's Name",
#     "Gender", "DOB(yyyy-mm-dd)", "Identification", "Date of Missing(yyyy-mm-dd)",
#     "Place of Residence"]
#     x = [data['Report-ID'],data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'],
#      data['Identification'], data['Date of Missing(yyyy-mm-dd)'], data["Place of Residence"] ]
#     filen = "Missing_People.csv"
#     with open(filen, 'w') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(field)
#         csvwriter.writerow(x)

# def insertData(data):
#     print(data['Name'])
#     rowId = 0
#     db = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
#     cursor = db.cursor()
#     print("Opened Database")

#     query = "INSERT INTO missing_data VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
#             (data["Report-ID"],data["Name"], data["Phone"], 
#              data["Father's Name"], data["Gender"], data["DOB(yyyy-mm-dd)"],
#              data["Identification"], data["Date of Missing(yyyy-mm-dd)"], data['Place of Residence'])

#     cursor.execute(query)
#     db.commit()
#     rowId = cursor.lastrowid
#     print("RowId %d" % rowId)

#     print("Record Created")
#     db.close()
#     return rowId

