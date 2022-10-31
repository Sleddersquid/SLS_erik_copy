
from db import Loans, Users, session
from datetime import datetime


new_user1 = Users(
    student_nr = "245614",
    name = 'Theo'
)
session.add(new_user1)

new_user2 = Users(
    student_nr = "574114",
    name = 'Hannes'
)
session.add(new_user2)


new_user3 = Users(
    student_nr = "314314",
    name = 'Aditi'
)
session.add(new_user3)


new_user4 = Users(
    student_nr = "462616",
    name = 'Nathanael'
)
session.add(new_user4)

date = datetime.now()


loans=[
    {
        "item_id": 1 ,
        "item_name": "Arduino" , 
        "student_nr" : "245614" ,
        "date": date
    },
        {
        "item_id": 2 ,
        "item_name": "raspbettypi" , 
        "student_nr" : "245614" ,
        "date": date
    },
        {
        "item_id": 3 ,
        "item_name": "Arduino" , 
        "student_nr" : "574114" ,
        "date": date
    },
        {
        "item_id": 4 ,
        "item_name": "raspbettypi" , 
        "student_nr" : "314314" ,
        "date": date
    },
        {
        "item_id": 5 ,
        "item_name": "raspbettypi" , 
        "student_nr" : "314314" ,
        "date": date
    },
        {
        "item_id": 6 ,
        "item_name": "Mus" , 
        "student_nr" : "245614" ,
        "date": date
    },
        {
        "item_id": 7 ,
        "item_name": "Pc skjerm" , 
        "student_nr" : "462616" ,
        "date": date
    },
        {
        "item_id": 8 ,
        "item_name": "Kaffekopp" , 
        "student_nr" : "462616" ,
        "date": date
    },
    
]


#users = session.query(Users).filter()

for i in loans :
    new_loan = Loans(
        item_id=i["item_id"],
        item_name=i["item_name"],
        student_nr=i["student_nr"],
        date=i["date"]
    )    
    session.add(new_loan)



session.commit()