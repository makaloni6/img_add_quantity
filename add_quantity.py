from PIL import Image, ImageDraw, ImageFont
import os

def textSetter():
    text_template = '{}\nx{}'
    font = ImageFont.truetype('ヒラギノ角ゴシック W3.ttc', 300)
    return text_template, font

def coverageCheck(bbox: list, xy: list):
    if float((bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (xy[0] * xy[1])) < 0.2:
        return True
    else:
        return False

def getImages()->list:
    

def getContent()->dict:
    pass

def main():
    text_template, font = textSetter()
    imgs = getImages()
    contents = getContent(img)
    errorImgs = []

    for img in imgs:
        img = Image.open('img/{}'.format(img_name))
        
        xy = list(img.size)
        draw = ImageDraw.Draw(img)

        content, q = contents[img]
        text = text_template.format(content, q)
        
        bbox = draw.multiline_textbbox((0, 0), text, font=font)
        
        if not coverageCheck(bbox, xy):
            errorImgs.append(img)
            continue
        
        # 描画
        draw.text((x - bbox[2], y - bbox[3]), text, font=font)
        img.save('img/{}.jpg'.format(img_name))

if __name__ == '__main__':
    main()
