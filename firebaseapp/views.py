from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config = {
    "apiKey": "AIzaSyALOzSxI2JTlwVELeLkeVllqzLONYL5JGQ",
    "authDomain": "fir-test-b7d33.firebaseapp.com",
    "databaseURL": "https://fir-test-b7d33-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "fir-test-b7d33",
    "storageBucket": "fir-test-b7d33.appspot.com",
    "messagingSenderId": "507677468583",
    "appId": "1:507677468583:web:53a95554b5fac0c0053882",
    "measurementId": "G-1RMF7QCVVR"
}


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()

def get_countries(request):
    items = []
    countries = db.child('countries').get()
    for country in countries.each():
        item = []
        item.append(country.val()['name'])
        items.append(item)
    context = {
        'items': items
    }

    return render(request=request, template_name='country_list.html', context=context)

def add_country(request):

    return render(request=request, template_name='add_country.html')

def post_country(request):
    path = str(request.build_absolute_uri())
    index = path.index('=')
    name = path[index + 1::]
    data = {'name': name}
    try:
        db.child('countries').push(data)
        message = 'Country {} is posted'.format(name)
        context = {
            'message': message
        }
    except:
        message = 'Unable to post country'
        context = {
            'message': message
        }


    return render(request=request, template_name='status.html', context=context)
