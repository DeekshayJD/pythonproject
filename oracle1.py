import cx_
try:
 con=cx_Oracle.connect('scott/tiger@localhost')
 cursor=con.cursor()
 cursor.execute("insert into employees values(100,'Durga',1000,'Hyd')")
 con.commit()
 print("Record Inserted Successfully")
except cx_Oracle.DatabaseError as e:
    if con:
     con.rollback()
     print("There is a problem with sql",e)
finally:
 if cursor:
  cursor.close()
 if con:
  con.close()