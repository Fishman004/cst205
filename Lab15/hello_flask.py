#Github Repo: https://github.com/Fishman004/cst205/tree/a39ca93b5df622628410994e430ecc9e0c9c3c87/Lab15


from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from data import one_pot_recipes
import random
from PIL import Image, ImageOps

images_paths = [
    "static/images/C3G9Wdh.jpg",
    "static/images/img1.jpg",
    "static/images/Untitled_drawing.png"
]

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

@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html', recipe_data = one_pot_recipes)

@app.route('/random')
def random_negative_image():
    random_path = random.choice(images_paths)
    original_img = Image.open(random_path)
    inverted_img = ImageOps.invert(original_img.convert("RGB"))
    inverted_img.save("static/images/negative.jpg")
    return '''
    <h1>Random Negative Image</h1>
    <img src="/static/images/negative.jpg" alt="Negative Image" />
    '''

@app.route('/starter')
def starter():
    return render_template('starter.html')

if __name__ == '__main__':
    app.run(debug=True)
