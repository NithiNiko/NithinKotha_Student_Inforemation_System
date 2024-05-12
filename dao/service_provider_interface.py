from entity.model import Courses,Enrollment,Payments,Students,Teachers
#from exceptions import Concurrency_control,Data_validation,Inventory_management,Order_processing,Payment_processing,Security_and_authentication
from util.db_conn_util import DBConnectivity

class ServiceProvider:
    def __init__(self):
        self.db_conn_util = DBConnectivity()

    def EnrollInCourse(self,enrollment_id,student_id,course_id,enrollment_date):
        try:
            conn=self.db_conn_util.makeconnection()
            cursor=conn.cursor()
            sql="INSERT into Enrollments (enrollment_id,student_id,course_id,enrollment_date) values (%s,%s,%s,%s) "
            values=(enrollment_id,student_id,course_id,enrollment_date)
            cursor.execute(sql,(values,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(str(e))
            return False
s=ServiceProvider()
s.EnrollInCourse(1,1,1,'2022-09-01')

