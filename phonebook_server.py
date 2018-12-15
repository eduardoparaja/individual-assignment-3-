from flask import Flask, jsonify

phonebook_server = Flask("phonebook")
        
phonebook = {"Eduardo": "65423420",
             "Satan":"666666666",
             "Girlfriend": "404"}


@phonebook_server.route("/home")
def see_phonebook():
    return jsonify(phonebook)
            
@phonebook_server.route("/add_contact/<name>/<number>", methods=["POST"])
def add_contact(name, number):   
   phonebook.update({name:number})
   return jsonify(str(name) + " was succesfully added to your phonebook")

@phonebook_server.route("/get_number/<name>")
def get_number_by_name(name):
    if name in phonebook:
        return jsonify(name + "'s number is: " + phonebook[name])

@phonebook_server.route("/delete_contact/<name>", methods=["DELETE"])
def delete_contact(name):   
    if name in phonebook: 
        del phonebook[name]
        return jsonify(name + "'s number was deleted from your phonebook.")         
 
@phonebook_server.route("/update_contact/<name>/<number>", methods=["PUT"])
def update_contact(name, number): 
    if name in phonebook: 
        phonebook[name] = number
        return jsonify(name + "'s number was updated, new number is: " + number)
    
  
   
phonebook_server.run()