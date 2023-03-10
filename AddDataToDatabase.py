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
        }
}
for key, value in data.items():
    ref.child(key).set(value)
