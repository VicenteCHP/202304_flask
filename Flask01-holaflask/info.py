from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo!"

@app.route('/users/<username>/<id>') 
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__ == "__main__":
    app.run(debug=True, port=8000)

