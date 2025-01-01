import os
from PIL import Image, ImageDraw, ImageFont

def create_image_from_text(text, filename="todo_image.png"): #creates an image and names it todo_image.png, puts it in current directory
    width, height = 1920, 1080
    image = Image.new('RGB', (width, height), color=(20, 20, 20)) #set background color
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype("/path/to/your/font/font.ttf", 40) #path to the font, size of font
    except IOError:
        font = ImageFont.load_default()
        
    x, y = 50, 50  #starting position of text
    line_height = 50
    for line in text.splitlines():
        draw.text((x, y), line, font=font, fill=(225, 225, 225)) #set text color
        y += line_height
    image.save(filename) #save the image to a file
    return filename

def read_todo_txt(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text


def main():
    txt_filename = "/path/to/your/text/file.txt" #path to the text file
    todo_text = read_todo_txt(txt_filename)
    image_path = create_image_from_text(todo_text)

if __name__ == "__main__":
    main()
