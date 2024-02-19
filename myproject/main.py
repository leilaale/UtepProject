from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login_page.html")

@app.route("/main_page")
def main_page():
    return render_template("main_page.html")


if __name__ == "__main__":
    
    app.run(debug=True)
