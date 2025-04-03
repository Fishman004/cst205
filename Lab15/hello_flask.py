from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return '''
    <h1>Favorite Acronyms</h1>
    <p>James F.: lol - laugh out loud</p>
    <p>Dad: afaik - as far as I know</p>
    <p>Mom: ttyl - talk to you later</p>
    <p>Sister: idk - I don't know</p>
    <p>Kris: np - no problem</p>
    '''

@app.route('/james')
def james():
    return render_template('templates.html')

if __name__ == '__main__':
    app.run(debug=True)
