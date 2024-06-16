from flask import Flask, render_template, request
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Contact:
    name: str
    email: str

def newContact(name, email) -> Contact:
    return Contact(name, email)

Contacts: list[Contact] = [newContact("John", "jd@gmail.com"),
                           newContact("Clara", "cd@gmail.com")]

@app.route("/")
def main():
    return render_template("index.html", Contacts=Contacts) 

@app.route("/contacts", methods=['POST'])
def process():
    name = request.form.get("name")
    email = request.form.get("email")
    new_contact = newContact(name, email)

    Contacts.append(new_contact)

    return render_template("contact.html", Contacts=Contacts)

# run app
if __name__ == "__main__":
    app.run(debug=True)
