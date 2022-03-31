import pyrebase
 # for authentication to firebase
config={
    
    "databaseURL": "https://dfirebase-f6a32-default-rtdb.firebaseio.com",
   "apiKey": "AIzaSyAT_i0upkR4mTq1ZK7GGmSOmnRniPFdFs4",     
  "type": "service_account",
  "project_id": "dfirebase-f6a32",
  "private_key_id": "cb1d137b9efda944ade97cf71241a58f8834c09d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCcxGJ64t9AiXy+\neJja7D1/02U0Et67rKdz3Mhr5qJFjniznVEW+IDBocgClTsCuYSq62/KC0QUT2BY\nOPQUpX2ZVyfk4WFK+4GYHaiJlvHDtHxWLw1u+T3Lb8i0zwFJO07NrTD23nnQ930f\n0FV+UtN3/1aKW1nZR5sjeYDzxvL5aiyyPMRRNxzeeuz7Eht8kA/7QsMMj/G5+RJE\ncP0/97xLSpHtC2TihzLcggwzUnmG70EZ5NtjI4gze26tpeDAqigaG57Cvln1i3nu\niG25dyLoRqrd/wWugphxYOgb0eIabsGGWjoLJOKR1NJ2wj2ZBl5E3Fgs60vYgmx0\nsKU5Zik5AgMBAAECggEABQFeNZc90pUxNvGpy7+kPQsWXaHGm85o8FGZ0pwkDT19\nzBpXRvj7P3N3a+Gw5ybePgjTYmuWqmFYbaiv3mLkTjuSqgOqNBcwrZcw1OfNY1bF\na4kIEEWD/BVfHqrHWzu6CeYgPJmg4ROt2pCv0h854kh0TmmZRk87fFf6To5JHr6A\nw/riW97TYxnQ61lKFii/wyHwPkLjkdDd6+kaDabaZeVOiDiwohZ1ohPNB3a2pZG6\n8ZHBllVLb5ZnslMD0PuV+xP2EinO8aras+jT2hFOpiu4B4o3yPmUSnWenFdXVXfN\nc09XOFRANCJ8nW53y6VDkRyqM/G4hcDLVgW33aclgQKBgQDa7sQX8UHUfoD48f8U\nMAX3M1YaTDWsTtNXZAU8ZkRnq/+5ayNO41/hLKz4XJSH0Ya4JTZVt4g6WRCHPKkO\nLPn9HWnz3uZEmoiGp8je0f+KhrzEDNJKl9biGi9aWkxWlwzAWCvuUpAJREBwGany\nZ2Aw5A1GToSkZc9oVHHzAVN2GQKBgQC3TyrSk1GuLBQhxWTSZHozteppO0o0NFiY\nV6PZ9elmRSmjh7DOJeywvejiQhEvJpbmogP1ayWjwGDWWLzxaETRSmNZwyHnS/z4\nsDP+3BHnHE8226p1VIf0uum7BvTawLhy8cUEYAJ2hrCdV6P67ITQK0GLCOyPp+ER\nHdpEbuFwIQKBgGqAZkIjadu+Im14A5dFeVF01rj6Q83rlqHXlTh5o2MvZ7pCZS22\nLGk0u3wiRVsA0WF5MMJoAswnkYPIPZEYzg+UpHsu/qN27V1b97p1O7OesetJNW92\nB+F7zXdNn/8rgdd7zPsljM4FNreRtHuoUEHYXqDKB3qV0Fy3X6tQBNLZAoGAZsNW\n+l3kOIQ1dQk4EEqLx1mAZCX8329JC352OMaHZfH3+dkj4S2Zlyuf1te60ngLuJez\nKG4816QNpZxxr9QIYFwXfkbKRuRumOwO+h1dW/ae4d4bnVMaNLRkO5kWw1uvC6FG\nFcHNH606bbqoDw9xFVJqmAsUsyQmJHZb2mlesIECgYEAiakM3quqb8fN0wa2fSE0\nuvs3Gs6s9iu1VoC56+mX4nYwBxrKYMFKBiwqL6u8fbEGJgLRhB7Kv//8cX0q1FAx\ncEI0oCUbEC+ZSsyZAXg50huOWtU7p0rT4/7WdoDVUdH9biRFX8Lz7PiXS2WSudIw\ncHNBBYenxNDaZhG6CHc9Km4=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-rr4tb@dfirebase-f6a32.iam.gserviceaccount.com",
  "client_id": "107273806711666071449",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "authDomain": "dfirebase-f6a32.firebaseapp.com",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rr4tb%40dfirebase-f6a32.iam.gserviceaccount.com",
  "storageBucket": "dfirebase-f6a32.appspot.com",
  "messagingSenderId": "128974347538",
  "appId": "1:128974347538:web:66b1c3c1bd1d84a983e7cb",
  "measurementId": "G-FTZL8SY5YC", 

  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCcxGJ64t9AiXy+\neJja7D1/02U0Et67rKdz3Mhr5qJFjniznVEW+IDBocgClTsCuYSq62/KC0QUT2BY\nOPQUpX2ZVyfk4WFK+4GYHaiJlvHDtHxWLw1u+T3Lb8i0zwFJO07NrTD23nnQ930f\n0FV+UtN3/1aKW1nZR5sjeYDzxvL5aiyyPMRRNxzeeuz7Eht8kA/7QsMMj/G5+RJE\ncP0/97xLSpHtC2TihzLcggwzUnmG70EZ5NtjI4gze26tpeDAqigaG57Cvln1i3nu\niG25dyLoRqrd/wWugphxYOgb0eIabsGGWjoLJOKR1NJ2wj2ZBl5E3Fgs60vYgmx0\nsKU5Zik5AgMBAAECggEABQFeNZc90pUxNvGpy7+kPQsWXaHGm85o8FGZ0pwkDT19\nzBpXRvj7P3N3a+Gw5ybePgjTYmuWqmFYbaiv3mLkTjuSqgOqNBcwrZcw1OfNY1bF\na4kIEEWD/BVfHqrHWzu6CeYgPJmg4ROt2pCv0h854kh0TmmZRk87fFf6To5JHr6A\nw/riW97TYxnQ61lKFii/wyHwPkLjkdDd6+kaDabaZeVOiDiwohZ1ohPNB3a2pZG6\n8ZHBllVLb5ZnslMD0PuV+xP2EinO8aras+jT2hFOpiu4B4o3yPmUSnWenFdXVXfN\nc09XOFRANCJ8nW53y6VDkRyqM/G4hcDLVgW33aclgQKBgQDa7sQX8UHUfoD48f8U\nMAX3M1YaTDWsTtNXZAU8ZkRnq/+5ayNO41/hLKz4XJSH0Ya4JTZVt4g6WRCHPKkO\nLPn9HWnz3uZEmoiGp8je0f+KhrzEDNJKl9biGi9aWkxWlwzAWCvuUpAJREBwGany\nZ2Aw5A1GToSkZc9oVHHzAVN2GQKBgQC3TyrSk1GuLBQhxWTSZHozteppO0o0NFiY\nV6PZ9elmRSmjh7DOJeywvejiQhEvJpbmogP1ayWjwGDWWLzxaETRSmNZwyHnS/z4\nsDP+3BHnHE8226p1VIf0uum7BvTawLhy8cUEYAJ2hrCdV6P67ITQK0GLCOyPp+ER\nHdpEbuFwIQKBgGqAZkIjadu+Im14A5dFeVF01rj6Q83rlqHXlTh5o2MvZ7pCZS22\nLGk0u3wiRVsA0WF5MMJoAswnkYPIPZEYzg+UpHsu/qN27V1b97p1O7OesetJNW92\nB+F7zXdNn/8rgdd7zPsljM4FNreRtHuoUEHYXqDKB3qV0Fy3X6tQBNLZAoGAZsNW\n+l3kOIQ1dQk4EEqLx1mAZCX8329JC352OMaHZfH3+dkj4S2Zlyuf1te60ngLuJez\nKG4816QNpZxxr9QIYFwXfkbKRuRumOwO+h1dW/ae4d4bnVMaNLRkO5kWw1uvC6FG\nFcHNH606bbqoDw9xFVJqmAsUsyQmJHZb2mlesIECgYEAiakM3quqb8fN0wa2fSE0\nuvs3Gs6s9iu1VoC56+mX4nYwBxrKYMFKBiwqL6u8fbEGJgLRhB7Kv//8cX0q1FAx\ncEI0oCUbEC+ZSsyZAXg50huOWtU7p0rT4/7WdoDVUdH9biRFX8Lz7PiXS2WSudIw\ncHNBBYenxNDaZhG6CHc9Km4=\n-----END PRIVATE KEY-----\n",

  "client_email": "firebase-adminsdk-rr4tb@dfirebase-f6a32.iam.gserviceaccount.com",
  "client_id": "107273806711666071449",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rr4tb%40dfirebase-f6a32.iam.gserviceaccount.com"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 
# for read the values of from firebase  

d = database.child('DDs').get().val()

context={

    'd' : d
}
print('getting the data = ',context)


# for adding the data  from python to firebase

data = {"Name": 'dd',"Value":'dd'}
# d=database.child('DDs').push(data)
d=database.child('DDs').child('ddd').set(data)
# d=database.child('xyzabc').set(data)

# for update the data from python to firebase
data = {"Name": 'kevin',"Value":'7777'}
d=database.child('DDs').child('-MsdrStjrRj2NtFbsDQg').update(data)

# # for remove the data from python to firebase
d=database.child('DDs').child('-MsdqinFrUl0wUoqNGD6').remove()

# day = database.child('Data').child('Day').get().val()
# id = database.child('Data').child('Id').get().val()
# projectname = database.child('Data').child('Projectname').get().val()
# return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })