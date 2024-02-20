from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://angel:angel123@cluster0.hi3uuvt.mongodb.net/?retryWrites=true&w=majority')
db = client['test_db']
proposals_collection = db['proposals']

@app.route("/")
def login():
    return render_template("login_page.html")

@app.route("/main_page", methods=['GET','POST'])
def main_page():
    if request.method == 'POST':
        proposal = request.files['file']
    
        db.proposals.insert_one({f'{proposal.filename}' : proposal.read()})

        return render_template('main_page.html', filename=proposal.filename)
    
    return render_template("main_page.html")

@app.route("/user_management")
def user_management():
     return render_template("admin_usr_mgmt.html")
     
@app.route("/test_page")
def test_page():
        return render_template("test_page.html")

if __name__ == "__main__":
    app.run(debug=True)
