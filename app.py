from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("welcome.html")
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST','GET'])
def register ():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        new_user = User(username = username,
                        password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for("home"))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)