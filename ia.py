
import ollama
from os import listdir
from os.path import isfile, join

def get_images_paths(folder_path):
    images_livre = ['./images/' + image for image in listdir(folder_path) if isfile(join(folder_path, image))]
    return images_livre

def generate_story(path):
    res = ollama.chat(
        model='llava',
        messages=[
            {
                'role': 'user', 
                'content': 'Generate a title and a fun 3 lines children story based on this image. ',
                'images': [path]
            }
        ],
    )

    return res['message']['content']



if __name__ == "__main__":
    
    images_livre = get_images_paths('static/images')

    for image in images_livre:
        story = generate_story(image)
        print(story)
        print('\n-----------------\n')





