from flask import Flask, render_template, request, redirect, url_for,flash
import secrets
from pymongo import MongoClient
import Word
import keyBertExtraction as kb

app = Flask(__name__)

#generate key everytime since users will be stored locally 
app.secret_key = secrets.token_hex(16)


# Database connection
client = MongoClient('mongodb+srv://angel:angel123@cluster0.hi3uuvt.mongodb.net/?retryWrites=true&w=majority')
db = client['test_db']
proposals_collection = db['proposals']
keywords_collection = db['keywords']
file_collection = db['files']


users = {
    'adminUser': {'password': 'adminPass', 'role': 'admin'},
    'regularUser': {'password': 'userPass', 'role': 'user'}
}

@app.route("/", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Directly check against a known username and password for debugging
        if username == 'testUser' and password == 'testPass':
            flash("Login successful!")
            return redirect(url_for('main_page'))  
        else:
            flash("Invalid username or password")

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
        
        # extracts keywords from document using keyBert 
        
        key_list = kb.keywordExtraction(proposal)
        
        for word in key_list:
          
          # Checks if word exist in the Database, returns 1 if it does
          
          word_Exist = keywords_collection.count_documents({"word" : word})
          
          if word_Exist == 0:   
               # Adds new keyword to keyword database
               
               newKey = Word.Word(word, proposal.filename)
               keywords_collection.insert_one({"word" : newKey.word, "appearances": newKey.appearances, "listOfFiles": newKey.listOfFiles})
          else: 
               
               # This updates number of appearances      
          
               q = {"word" : word}
               getWord = keywords_collection.find_one(q)
               n = getWord['appearances']
               newValues = { "$set": { "appearances": n+1 } }
               keywords_collection.update_one(q, newValues)
               
               # Updates listOfFiles Array 
               
               q = {"word" : word}
               getWord = keywords_collection.find_one(q)
               n = getWord['listOfFiles']
               
               if proposal.filename not in n:
                    keywords_collection.update_one({"word" : word}, { "$push" : { "listOfFiles" : proposal.filename}})
               
      
        #print("HEEEEEEEEEEEEEEEEEREEEEEE")
        n = proposal.read()
        #print(n)
        #file_collection.insert_one({f'proposal.filename' : proposal.read()})
        #file_collection.insert_one({"File Name" : proposal.filename, "PDF" : n})
        file_collection.insert_one({"File Name": proposal.filename, "Keyword List": key_list, "PDF": n})
        
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
