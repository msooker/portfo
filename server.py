from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        messege = data['messege']
        csv_writer = csv.writer(database2, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, messege])

@app.route('/apitest', methods=['POST', 'GET'])
def apitest():
   if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/Thank you.html')
        except:
            return "something went wrong"
   else:
        return 'Error'