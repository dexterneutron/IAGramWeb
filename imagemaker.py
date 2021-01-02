from db import RamdomQuote,GetQuotesList,QuotebyId,InsertOutput
from imageLoader import RandomImage
from PIL import Image,ImageFont
from IAgram import IATransform, RandomTransform
import time
OUTPUTPATH="static/Output/"
PUBLICPATH="Output/"

size=612,612
        

def SpecificTransform(imageid,quoteid,effect):
        start_time = time.time()
        f,a=QuotebyId(quoteid)
        index=0
        start_time = time.time()
        sentence=f if a=="" else "{quote}. -{author}".format(quote=f,author=a)
        i=Image.open(ImagebyId(imageid))
        i=i.resize(size)
        img=IATransform(effect,sentence,i)
        imgpath="{path}image{i}.png".format(path=OUTPUTPATH,i=index)
        print(imgpath)
        img.save(imgpath)  
        print('All Images generated')
        print('Execution Time: ')
        print("--- %s seconds ---" % (time.time() - start_time))

def AllImages():
        q=GetQuotesList()
        index=0
        start_time = time.time()
        for q in q:
                quoteid=(q['_id'])
                f=(q['Frase'])
                a=(q['Autor'])
                sentence=f if a=="" else "{quote}. -{author}".format(quote=f,author=a)
                background=RandomImage()
                i=Image.open(background)
                i=i.resize(size)
                filter=RandomTransform()
                img=IATransform(filter,sentence,i)
                imgFilePublic="{path}image{i}.png".format(path=PUBLICPATH,i=index)
                imgpath="{path}image{i}.png".format(path=OUTPUTPATH,i=index)
                print(imgpath)
                img.save(imgpath)
                index+=1
                InsertOutput(quoteid,background,filter,imgFilePublic)
        print('All Images generated')
        print('Execution Time: ')
        print("--- %s seconds ---" % (time.time() - start_time))

