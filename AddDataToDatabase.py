import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-1e56a-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "Name: ": "Katy Perry",
            "Major: ": "Singer",
            "Starting Year: ": 2005,
            "Total Attendance: ": 6,
            "Standing: ": "G",
            "Year: ": 4,
            "Last Attendance: ": "2023-03-10 11:36:00"
        },

    "852741":
        {
            "Name: ": "Lewis Hamilton",
            "Major: ": "Racer",
            "Starting Year: ": 2007,
            "Total Attendance: ": 8,
            "Standing: ": "A",
            "Year: ": 16,
            "Last Attendance: ": "2023-03-10 11:39:11"
        },

    "963852":
        {
            "Name: ": "Abdul Ahad",
            "Major: ": "AI",
            "Starting Year: ": 2018,
            "Total Attendance: ": 9,
            "Standing: ": "F",
            "Year: ": 3,
            "Last Attendance: ": "2023-03-10 11:49:18"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
