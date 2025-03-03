from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index_new.html :: Flask app this is ...'
    #return "New"

if __name__ == '__main__':
    app.run(debug=True)
