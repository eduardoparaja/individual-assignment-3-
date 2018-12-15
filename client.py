import requests

def see_phonebook(): 
    request = requests.get('http://127.0.0.1:5000/home') 
    return request.json() 

def add_contact(name, number): 
    request = requests.post('http://127.0.0.1:5000/add_contact/{}/{}'.format(name, number))
    return request.json()

def get_number_by_name(name): 
    request = requests.get('http://127.0.0.1:5000/get_number/{}'.format(name))
    return request.json()

def delete_contact(name): 
    request = requests.delete('http://127.0.0.1:5000/delete_contact/{}'.format(name))
    return request.json()

def update_contact(name, number):
    request = requests.put('http://127.0.0.1:5000/update_contact/{}/{}'.format(name, number))
    return request.json()