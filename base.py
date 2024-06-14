from flask import Flask, render_template, render_template_string, request
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Contact:
    name: str
    email: str

def newContact(name, email) -> Contact:
    return Contact(name, email)

Contacts: list[Contact] = []

Contacts.append(newContact("John", "jd@gmail.com"))
Contacts.append(newContact("Clara", "cd@gmail.com"))

@app.route("/", methods=['GET'])
def main():
    return render_template("base.html", Contacts=Contacts)

@app.route("/contacts", methods=['GET', 'POST'])
def contacts():
    name = request.form.get("name")
    email = request.form.get("email")
    new_contact = newContact(name, email)
    Contacts.append(new_contact)

    print(f"New contact: {new_contact}")
    return render_template("base.html", Contacts=Contacts)

if __name__ == "__main__":
    app.run(debug=True)
