
from pymysql import Connection
import time 

class EmailService(Connection):
    def __init__(s):
        s.db = Connection(host="localhost",user="root",password="12345678",database="newsletter")
        s.cur = s.db.cursor()


        s.emails = {}
        s.emailLimit = {}
        s.emailUniqueness = {}

        s.cur.execute("select * from details")
        for i in s.cur:
            if i[0] not in s.emails.keys():
                s.emails[i[0]] = i[1]
            if i[0] not in s.emailLimit.keys():
                s.emailLimit[i[0]] = i[2]
            if i[0] not in s.emailUniqueness.keys():
                s.emailUniqueness[i[0]] = i[3]

        print(s.emails)
        print(s.emailLimit)
        print(s.emailUniqueness)
        print()
        print()


class mockEmail_1(EmailService):
    def __init__(s):
        super().__init__()
             
        s.unique = input("Assign an alphabet for this email: ")
        s.failedEmailsfromMock1 =[]


        for i in s.emailUniqueness.items():
            if s.unique not in i[1]:
                
                if s.emailLimit[i[0]]<5:
                    
                    print("*******Sending from Mock Email 1*******\n")
                    time.sleep(1)
                    print("Sending email to ",i[0],".......\n")
                    time.sleep(1)
                    emailSendingAttempt = 1
                    responseFromRecepient = ""
                    failure = True
                    
                    while emailSendingAttempt<4:
                        responseFromRecepient = input("Press 'y' if the email is sent successfully/or any other key for failure: ")
                        if responseFromRecepient == "y":
                            s.emailUniqueness[i[0]]+= s.unique
                            s.emailLimit[i[0]]+=1
                            time.sleep(1)
                            print("Email Successfully sent to ",i[0],"from mock Email provider 1\n")
                            failure = False
                            break
                        else:
                            if emailSendingAttempt == 1:
                                print("Retrying in 2 seconds.....")
                                time.sleep(2)

                            if emailSendingAttempt == 2:
                                print("Retrying in 4 seconds.....")
                                time.sleep(4)
                                
                            if emailSendingAttempt == 3:
                                print("Retrying in 8 seconds.....")
                                time.sleep(8)
                                
                        emailSendingAttempt+=1
                        
                    if failure:
                        s.failedEmailsfromMock1.append(i[0])
                        
                    
                else:
                    print("Cannot send anymore emails to ",i[0]," Try again after 24 hours\n")
            else:
                print(i[0],"has already received this email\n")
            
        
class mockEmail_2(mockEmail_1):
    def __init__(s):
        super().__init__()
        s.failedEmailsfromMock2 =[]

        
        if len(s.failedEmailsfromMock1)>0:
            for j in s.emailUniqueness.items():
                if j[0] in s.failedEmailsfromMock1:
                    print("*******Sending from Mock Email 2*******\n")
                    time.sleep(1)
                    print("Sending email to ",j[0],".......\n")
                    time.sleep(1)
                    emailSendingAttempt = 1
                    responseFromRecepient = ""
                    failure = True
                    
                    while emailSendingAttempt<4:
                        responseFromRecepient = input("Press 'y' if the email is sent successfully/or any other key for failure: ")
                        if responseFromRecepient == "y":
                            s.emailUniqueness[i[0]]+= s.unique
                            s.emailLimit[j[0]]+=1
                            time.sleep(1)  
                            print("Email Successfully sent to ",j[0],"from mock Email provider 2")
                            failure = False
                            break
                        else:
                            if emailSendingAttempt == 1:
                                print("Retrying in 2 seconds.....")
                                time.sleep(2)

                            if emailSendingAttempt == 2:
                                print("Retrying in 4 seconds.....")
                                time.sleep(4)
                                
                            if emailSendingAttempt == 3:
                                print("Retrying in 8 seconds.....")
                                time.sleep(8)
                                
                        emailSendingAttempt+=1
                    if failure:
                        s.failedEmailsfromMock2.append(j[0])

class SendEmail(mockEmail_2):
    def __init__(s):
        super().__init__()

        if len(s.failedEmailsfromMock2)!=0:
            print("Cannot send email to ",s.failedEmailsfromMock2, "Try again!\n")

        s.query1 = "UPDATE details SET limits = %s WHERE c_names = %s"

        for m,n in s.emailLimit.items():
            s.cur.execute(s.query1,(n,m))
            s.db.commit()

        s.query2 = "UPDATE details SET uniqueness = %s WHERE c_names = %s"

        for o,p in s.emailUniqueness.items():
            s.cur.execute(s.query2,(p,o))
            s.db.commit()

        print("Details Updated to Database!")


class Clear(Connection):
    def __init__(s):
        s.db = Connection(host="localhost",user="root",password="12345678",database="newsletter")
        s.cur = s.db.cursor()
        
        lReset = {'lilly': 0, 'tom': 0, 'john': 0}
        uReset = {'lilly': ' ', 'tom': ' ', 'john': ' '}
        
        s.query3 = "UPDATE details SET limits = %s WHERE c_names = %s"

        for q,r in lReset.items():
            s.cur.execute(s.query3,(r,q))
            s.db.commit()

        s.query4 = "UPDATE details SET uniqueness = ' ' WHERE c_names = %s"

        for u in uReset.keys():
            s.cur.execute(s.query4,(u,))
            s.db.commit()

        print("Counter reset back to zero successfull")
        



e = SendEmail()


        

        
        

        
    
    
                    
                
                
            
    

        
    
        
           




