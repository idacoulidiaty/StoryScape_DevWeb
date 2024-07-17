
import ollama
from os import listdir
from os.path import isfile, join



images_livre = ['./images/' + image for image in listdir('images') if isfile(join('images', image))]
print (images_livre)


#image_path = './static/images/ptit_chaperon.jpeg'

res = ollama.chat(
    model='llava',
    messages=[
      {
        'role': 'user', 
        'content': 'Describe the images in this list',
        'images': [image for image in range(len (images_livre))]
        }
    ],
)


print(res['message']['content'])