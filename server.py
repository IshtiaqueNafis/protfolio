from flask import Flask, render_template, url_for, request, redirect  # this is the needed package
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")  # making it more dynamic so each time a page is created page_name is clicked
def about(page_name):  # page name is the parameter
    return render_template(page_name)  # page will load based on the page parameter


def write_to_file(data):
    with open('datafile.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):  # data is the dictionary that is being passed
    with open('database.csv',newline="", mode='a') as database: # this creates a new line
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
