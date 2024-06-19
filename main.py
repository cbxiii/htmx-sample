from flask import Flask, render_template, request, abort
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Contact:
    name: str
    email: str
    id: int

class Contacts:
    def __init__(self):
        self.contacts: list[Contact] = []
        self.id: int = 0

    def newContact(self, name, email) -> Contact:
        self.id += 1
        new_contact = Contact(name, email, self.id)
        self.contacts.append(new_contact)
        return new_contact
    
    def removeContact(self, id) -> bool:
        index = self.indexOf(id)
        if index != -1:
            del self.contacts[index]
            return True
        else:
            return False

    def indexOf(self, id) -> int:
        for i, c in enumerate(self.contacts):
            if c.id == id:
                return i
        return -1

    def get_contacts(self) -> list[Contact]:
        return self.contacts

contact_list = Contacts()
contacts = contact_list.get_contacts()

@app.route("/")
def main():
    return render_template("index.html", contacts=contacts) 

@app.route("/contacts", methods=['POST'])
def process():
    name = request.form.get("name")
    email = request.form.get("email")

    if any(contact.email == email for contact in contacts):
        abort(422, description="Email already exists...")

    contact_list.newContact(name, email) 

    return render_template("contacts.html", contacts=contacts)

@app.route("/contacts/<int:id>", methods=['DELETE'])
def delete_contact(id):
    if not contact_list.removeContact(id):
        return "contact not found...", 404
    contacts = contact_list.get_contacts()
    return render_template("contacts.html", contacts=contacts)

@app.errorhandler(422)
def bad_request(error):
    render_template("contacts.html", contacts=contacts)
    return render_template("form.html", error=error.description), 422

# run app
if __name__ == "__main__":
    app.run(debug=True)
