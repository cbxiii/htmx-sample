from flask import Flask, render_template, render_template_string
from multiprocessing import Value

app = Flask(__name__)
counter = Value('i', 0)


@app.route("/")
def main():
    return render_template("index.html", count=counter.value) 

@app.route("/count", methods=['GET', 'POST'])
def process():
    with counter.get_lock():
        counter.value += 1
        count = counter.value 
    return render_template_string('<div id="count">Count: {{ count }}</div>', count=count) 


# run app
if __name__ == "__main__":
    app.run(debug=True)
