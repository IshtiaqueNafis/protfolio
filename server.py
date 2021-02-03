import csv

from flask import Flask, render_template, request, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
    


def write_to_csv(data):  # data is the dictionary that is being passed
    with open('database.csv', newline="", mode='a') as database:  # this creates a new line
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writter = csv.writer(database, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)  # constructor for creating csv_writter
        csv_writter.writerow([email, subject, message])


@app.route('/sent_data', methods=['POST', 'GET'])
def sent_data():
    if request.method == 'POST':
        data = request.form.to_dict()  # this converts it to dictionary
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong"


if __name__ == "__main__":
    app.debug = True
    app.run()
