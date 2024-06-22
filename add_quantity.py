from PIL import Image, ImageDraw, ImageFont  # type: ignore
import csv
import os
import re
import pickle


def textSetter():
    text_template = '{}\nx{}'
    font = ImageFont.truetype('ヒラギノ角ゴシック W3.ttc', 100)
    return text_template, font


def coverageCheck(bbox: list, xy: list):
    if float((bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (xy[0] * xy[1])) < 0.2:
        return True
    else:
        return False


def getImages() -> list:
    files = os.listdir('./imgs/')
    return files


def getContent() -> dict:
    with open('./pickle/contents.pickle', 'rb') as f:
        contents = pickle.load(f)

    with open('title_fixed.csv', 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    
    for d in data:
        contents[d[0]] = [d[1], d[2]]

    return contents


def getCodes(acc: str) -> dict:
    with open('./pickle/code_dict_{}.pickle'.format(acc), 'rb') as f:
        code_dict = pickle.load(f)
    return code_dict


def main():
    acc = input()
    text_template, font = textSetter()
    imgs = getImages()
    contents = getContent()
    code_dict = getCodes(acc)
    errorImgs = []

    for img_name in imgs:

        img = Image.open('./imgs/{}'.format(img_name))
        id = img_name[:-4]

        xy = list(img.size)
        if xy[0] > 2000:
            font = ImageFont.truetype('ヒラギノ角ゴシック W6.ttc', index=3, size=300)
        else:
            font = ImageFont.truetype('ヒラギノ角ゴシック W6.ttc', index=3, size=200)
        draw = ImageDraw.Draw(img)

        if id not in contents:
            continue
        if id not in code_dict:
            continue
        content, q = contents[id]
        if 'リットル' in content:
            content = re.findall(r'[0-9.]+', content)[0] + 'L'
        text = text_template.format(content, q)

        bbox = draw.multiline_textbbox((0, 0), text, font=font)

        if not coverageCheck(bbox, xy):
            errorImgs.append(img)
            continue

        # 描画
        draw.text((xy[0] - bbox[2] - 50, xy[1] - bbox[3] - 50), text, 'black', font=font)

        img_name = code_dict[id]

        img.save('modifiedImgs/{}.jpg'.format(img_name))

    with open('error.pickle', 'wb') as f:
        pickle.dump(errorImgs, f)
    print(len(errorImgs))
    print('finished {}'.format(acc))


if __name__ == '__main__':
    main()
