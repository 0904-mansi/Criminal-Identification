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
    print(data['Criminal-ID'])
    rowId = 0
    db = pymysql.connect(host="localhost",user="root",password="",database="criminaldb")
    cursor = db.cursor()
    print("Opened Database")
    print("Database Connected successfully")
    query = "INSERT INTO criminaldata VALUES('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Criminal-ID"], data["Address"], data["Phone"], data["Name"],
             data["Father's Name"], data["Gender"], data["DOB(yyyy-mm-dd)"],
             data["Crimes Done"], data["Date of Arrest(yyyy-mm-dd)"], data["Place of Arrest"])

    cursor.execute(query)
    db.commit()
    rowId = cursor.lastrowid
    # print("RowId %d" % rowId)
    print("data stored on new row in the database")



    print("Record Created")
    db.close()
    return rowId


