
from flask import Flask
from flask import render_template
from os import listdir
from os.path import isfile, join


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/gallery")
def gallery():
    images_livre = ['images/' + image for image in listdir('images') if isfile(join('images', image))]
    return render_template('gallery.html', images=images_livre)



if __name__ == "__main__":
    app.run(debug=True)