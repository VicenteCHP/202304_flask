from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/tabla')
def tabla():
    return render_template('tabla.html')

if __name__ == '__main__':
    app.run(debug=True)