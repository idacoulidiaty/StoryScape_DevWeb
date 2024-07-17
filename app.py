
from flask import Flask
from flask import render_template
from os import listdir
from os.path import isfile, join

from ia import *


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/gallery")
def gallery():
    images_livre = get_images_paths('static/images')
    image_path_and_stories = []
    for image in images_livre:
        story = generate_story(image)
        image_html = '../' + image
        image_path_and_stories.append( (story, image_html) )

    return render_template('gallery.html', images=images_livre)



if __name__ == "__main__":
    app.run(debug=True)

