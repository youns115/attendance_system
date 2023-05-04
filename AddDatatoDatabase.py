import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("./venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://attendancesystem-d8468-default-rtdb.europe-west1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    '448865':
        {
            "name": "Jordan Peterson",
            "major": "Psychology",
            "starting_year":2017,
            "total_attendance":6,
            "standing": "Legend",
            "year":4,
            "Last_attendance_time": "2022-12-11 00:54:34"


        },
    '987869':
        {
            "name": "Lou Bloom",
            "major": "Fine Arts",
            "starting_year":2018,
            "total_attendance":11,
            "standing": "Monster",
            "year":3,
            "Last_attendance_time": "2023-6-10 00:54:34"


        }
}

for key,value in data.items():
    ref.child(key).set(value)