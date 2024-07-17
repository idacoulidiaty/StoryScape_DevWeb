
import ollama
from os import listdir
from os.path import isfile, join



images_livre = ['./images/' + image for image in listdir('images') if isfile(join('images', image))]
#print (images_livre)


#image_path = './static/images/ptit_chaperon.jpeg'

descriptions = []


for image in images_livre:
    res = ollama.chat(
        model='llava',
        messages=[
            {
                'role': 'user', 
                'content': 'Generate a title and a fun and short children story based on this image',
                'images': [image]
            }
        ],
    )
    
   
    descriptions.append(res['message']['content'])


for description in descriptions:
    print(description)




