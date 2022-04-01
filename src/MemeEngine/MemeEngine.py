from PIL import Image
import os
import textwrap
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """Combine image and quote for meme"""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)


    def make_meme(self, img_path, body = None, author = None, width=500) -> str:
        """"access and edit image and write quote on image. Return path to new image"""
        try:
            # resize image
            img = Image.open(img_path)
            if width > 500:
                width = 500
                height = round(img.size[1] * ratio)
                ratio = width/img.size[0]
                img = img.resize((width, height), Image.NEAREST)

            # wrapper and font
            wrapper = textwrap.TextWrapper(width=30)
            full_quote=wrapper.fill(text=f'"{body}" - {author}')
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=30)

            # range limit to prevent text from going outside of the image
            x = random.randint(1, 100)
            y = random.randint(1, 300)

            # draw quote
            draw.multiline_text((x, y), full_quote, font=font)

            # save image
            rand_num = random.randint(1,10000)
            output_path = os.path.join(self.output_dir, f'./{rand_num}.jpg')
            img.save(output_path)

        except(FileNotFoundError):
            raise ValueError('Unable to find file')
        except(TypeError):
            raise TypeError('Invalid file')

        return output_path
