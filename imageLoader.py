import os, random,glob

IMG_PATH="Backgrounds/"
OUTPUT_PATH="static/Output"
def RandomImage():
    img=random.choice(os.listdir(IMG_PATH))
    return IMG_PATH+img

def ImagebyId(id):
    img="background{i}.jpg".format(i=id)
    return IMG_PATH+img

def DeleteAllImages():
    files = glob.glob(OUTPUT_PATH)
    for f in files:
        os.remove(f)

