from flask import Flask, render_template
import glob
from ia import generate_story  # Assurez-vous que cette fonction est correctement importée

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    # Récupérer les chemins des images
    urls = glob.glob('static/images/*.jpeg')  # Adapter l'extension si nécessaire
    image_path_and_stories = []

    # Générer une histoire pour chaque image
    for url in urls:
        story = generate_story(url)  # Appeler la fonction pour générer l'histoire
        url_html = url.replace('static/', '')  # Adapter le chemin pour le HTML
        image_path_and_stories.append((story, url_html))

    return render_template('gallery.html', images=image_path_and_stories)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
