import random
import os
import requests
from flask import Flask, render_template, abort, request
from datetime import datetime

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from QuoteEngine import DocxIngestor
from QuoteEngine import QuoteModel


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    # parse files with ingestor class
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # find images
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


# call setup function to gather quotes and images
quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)  # select random image
    quote = random.choice(quotes)  # select random quote
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Creates a user defined meme """

    # get image URL
    img_url = request.form.get("image_url")
    img_content = requests.get(img_url, stream=True).content

    #create temporarty image file
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    rand_num = random.randint(1, 100000)
    t_img = f'./tmp/{rand_num}.png'
    with open(t_img, 'wb') as f:
        f.write(img_content)

    # get quote
    body = request.form.get('body', '')
    author = request.form.get('author', 'Anonymous')
    quote = QuoteModel(body=body, author=author)

    # generate new image
    path = meme.make_meme(t_img, quote.body, quote.author)\

    # remove image
    os.remove(t_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
