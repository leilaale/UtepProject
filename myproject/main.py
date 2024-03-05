from flask import Flask, render_template, request
from pymongo import MongoClient
import sample
import keyBertExtraction as kb
import json

app = Flask(__name__)
client = MongoClient('mongodb+srv://angel:angel123@cluster0.hi3uuvt.mongodb.net/?retryWrites=true&w=majority')
db = client['test_db']
proposals_collection = db['proposals']
keywords_collection = db['test_collection']
keywords = {}

#r = sample.Keyword('random', 'test')
#keywords_collection.insert_one({'random' : json.dumps(r.__dict__)})

@app.route("/")
def login():
    return render_template("login_page.html")

@app.route("/main_page")
def main_page():
    return render_template("main_page.html")

@app.route("/admin_dashboard")
def admin_dashboard():
     return render_template("admin_dashboard.html")

@app.route("/proposal_upload", methods=['GET','POST'])
def proposal_upload():
     if request.method == 'POST':
        proposal = request.files['file']
        
        key_list = kb.keywordExtraction(proposal)
        
        for word in key_list:
             
          if word not in keywords:   
               newKey = sample.Keyword(word, proposal)
               keywords[word] = newKey
               keywords_collection.insert_one({word : json.dumps(newKey.__dict__)})
          else: 
               keywords[word].searchFiles(proposal)
               #keywords[word].appearances += 1
               #keywords[word].listOfFiles.append(proposal)
        
        
        print("HERE")
        print(keywords.keys())
        
        #db.proposals.insert_one({f'{proposal.filename}' : sample.File(f'{proposal.filename}', proposal.read(), key_list)})
        
        return render_template('proposal_upload.html', filename=proposal.filename)
     
     return render_template("proposal_upload.html")


@app.route("/user_management")
def user_management():
     return render_template("admin_usr_mgmt.html")
     
@app.route("/test_page")
def test_page():
        return render_template("test_page.html")

if __name__ == "__main__":
    app.run(debug=True)
