from PIL import Image, ImageDraw,ImageFont,ImageFilter
import random

#COLOR CONSTANTS
BLACK=(0,0,0)
WHITE=(255,255,255)
#FILTER COLOR CONSTANTS
FILTER_BLUE=(6, 50,71)
FILTER_BROWN=(112, 66, 20)
FILTER_GREEN=(51,97,32)
FILTER_PURPLE=(87,10,84)
FILTER_GREYBLUE=(102,122,129)
FILTER_YELLOW=(60,61,29)
FILTER_LIGHTPURPLE=(41,0,62)
#FONTS CONSTANTS
FONTSPATH='Fonts/'
CROISSANT_ONE='CroissantOne-Regular.ttf'
MARCELLUS_REGULAR='MarcellusSC-Regular.ttf'
PHILOSOPHER='Philosopher-Bold.ttf'
RIBEYE='Ribeye-Regular.ttf'
VARIANE='variane-script.regular.ttf'
BROSHK='Broshk.ttf'
APPLETEA='AppleTea.ttf'

def IATransform(filter,sentence,i,color='ramdom'):
    if filter=='DarkWhiteText':
        fontfile=FONTSPATH+random.choice([CROISSANT_ONE,MARCELLUS_REGULAR,PHILOSOPHER,VARIANE])
        #fontfile=FONTSPATH+random.choice([HEYOCTOBER])
        fnt = ImageFont.truetype(fontfile, 50)
        brightness=0.3
        img=BrightnessFilter(i, brightness)
        img=AddcenteredText(sentence,img,fnt)
        return img
    elif filter=='ColourWhiteText':
        fontfile=FONTSPATH+random.choice([CROISSANT_ONE,MARCELLUS_REGULAR,PHILOSOPHER,VARIANE])
        #fontfile=FONTSPATH+random.choice([VARIANE])
        fnt = ImageFont.truetype(fontfile, 50)
        color=random.choice([FILTER_BLUE, FILTER_BROWN,FILTER_GREEN,FILTER_PURPLE,FILTER_GREYBLUE,FILTER_YELLOW,FILTER_LIGHTPURPLE])
        img=AddTransparentLayer(i,color)
        img=AddcenteredText(sentence,img,fnt)
        return img
    elif filter=='CenterWhiteBox':
        fontfile=FONTSPATH+random.choice([RIBEYE,BROSHK])
        #fontfile=FONTSPATH+random.choice([APPLETEA])
        fnt = ImageFont.truetype(fontfile, 50)
        img=AddcenteredText(sentence,i,fnt,fontcolor=BLACK,textbox=True)
        return img
    elif filter=='AlphaText':
        fontfile=FONTSPATH+random.choice([APPLETEA])
        fnt = ImageFont.truetype(fontfile, 50)
        img=AddTransparentText(sentence,i,fnt)
        return img
    else:
        print('Filter doesnt exist')

def AddcenteredText(sentence,img,fnt,fontcolor=WHITE,textbox=False):
    d = ImageDraw.Draw(img)
    x1 = 612
    y1 = 612
    sum=0
    for letter in sentence:
        sum += d.textsize(letter, font=fnt)[0]
        average_length_of_letter = sum/len(sentence)
        #find the number of letters to be put on each line
        number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
        incrementer = 0
        fresh_sentence = ''
    #add some line breaks
    for letter in sentence:
        if(letter == '-'):
            fresh_sentence += '\n\n' + letter
        elif(incrementer < number_of_letters_for_each_line):
            fresh_sentence += letter
        else:
            if(letter == ' '):
                fresh_sentence += '\n'
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer+=1
    fresh_sentence += '\n\n\n'+'@agooday4you'
    #print (fresh_sentence)
    #render the text in the center of the box
    dim = d.textsize(fresh_sentence, font=fnt)
    x2 = dim[0]
    y2 = dim[1]
    qx = (x1/2 - x2/2)
    qy = (y1/2-y2/2)
    #Uncomment to add font border
    #d.text((qx-1, qy), fresh_sentence, align="center",font=fnt, fill=(0,0,0))
    #d.text((qx+1, qy), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    #d.text((qx, qy-1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    #d.text((qx, qy+1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    if(textbox):
        front = Image.new('RGB', (x2+5, y2+15), color = WHITE)
        front.putalpha(100)
        img.paste(front,(int(qx),int(qy)),mask=front)
    d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=fontcolor)
    return img
def AddTransparentText(sentence,img,fnt,fontcolor=WHITE,textbox=False):
    size=612,612
    alphalayer=Image.new('L',size, (0))
    d = ImageDraw.Draw(alphalayer)
    x1 = 612
    y1 = 612
    sum=0
    for letter in sentence:
        sum += d.textsize(letter, font=fnt)[0]
        average_length_of_letter = sum/len(sentence)
        #find the number of letters to be put on each line
        number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
        incrementer = 0
        fresh_sentence = ''
    #add some line breaks
    for letter in sentence:
        if(letter == '-'):
            fresh_sentence += '\n\n' + letter
        elif(incrementer < number_of_letters_for_each_line):
            fresh_sentence += letter
        else:
            if(letter == ' '):
                fresh_sentence += '\n'
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer+=1
    fresh_sentence += '\n\n\n'+'@agooday4you'
    #print (fresh_sentence)
    #render the text in the center of the box
    dim = d.textsize(fresh_sentence, font=fnt)
    x2 = dim[0]
    y2 = dim[1]
    qx = (x1/2 - x2/2)
    qy = (y1/2-y2/2)
    #Uncomment to add font border
    #d.text((qx-1, qy), fresh_sentence, align="center",font=fnt, fill=(0,0,0))
    #d.text((qx+1, qy), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    #d.text((qx, qy-1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    #d.text((qx, qy+1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(255))
    
    #d.text((qx,y1-25), "@agooday4you" ,align="center",  font=fnt, fill=(255))
    img.putalpha(alphalayer)
    back = Image.new('RGB', (612, 612), color = WHITE)
    back.paste(img,(0,0),mask=img)
    return back

def BrightnessFilter(i, br):
    img = Image.new('RGB', i.size)
    for x in range(i.size[0]):
        for y in range(i.size[1]):
            r, g, b = i.getpixel((x, y))
            red = int(r * br)
            red = min(255, max(0, red))
            green = int(g * br)
            green = min(255, max(0, green))
            blue = int(b * br)
            blue = min(255, max(0, blue))
            img.putpixel((x, y), (red, green, blue))
    return img

def AddTransparentLayer(i,color):
    front = Image.new('RGB', (612, 612), color = color)
    front.putalpha(80)
    i.paste(front,(0,0),mask=front)
    return i

def RandomTransform():
    filters=["DarkWhiteText","ColourWhiteText","CenterWhiteBox","AlphaText"]
    return random.choice(filters)

