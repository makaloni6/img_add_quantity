from PIL import Image, ImageDraw, ImageFont

img = Image.open('img/test.jpg')

x, y = img.size
text = 'x30'
font = ImageFont.truetype('Arial.ttf', 300)
draw = ImageDraw.Draw(img)
draw.text((x - 600, y - 300), text, 'red', font=font)

img.save('img/test_after.jpg')