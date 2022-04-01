# meme generator
## Overview

This application is a dynamic application that generates images with quotes.
The purpose of this project is to create memes from a set of provided images and text
from various file types. It can accept files contained in a project module
(_data) and randomly assign quotes and images, as well as user generated text and image URLs.

### QuoteEngine module
This module contains files with classes that can parse the text in various files.
It can handle files with txt, pdf, docx, and csv extensions.
QuoteModel is the object which accepts the quote and author, which are extracted by
the various ingestors. There is a parent ingestor (IngestorInterface) which contains
A classmethod method to check whether the file is compatable with the ingestor class
and a parse method to parse the content in the files. It also has four
child ingestor classes for each file type. Ingestor.py uses an abstract method to field
the files to the right ingestor. Each class provides a list of QuoteModel objects
consisting of a text body and author.
Accepted file types and their dependancies are:
- docx (python-docx)
- csv (pandas)
- pdf (subprocess)
- txt (pandas)

### MemeEngine module

The meme engine module accepts the path to the photos and edits them to the
correct size (width = 500mp) and prints the text to the image. The placement of
the text is random, within a range. A new file is created and the path is returned.
Uses Flask and requests to fetch an image from a user submitted URL

### meme.py
Finds images and texts and applies ingestor class returning the list of images and
quotes. Chooses the quotes and images randomly and makes meme.
CLI module accepts three arguments that can be entered from the command line so that
a user can create the meme:
--body a string quote body
--author a string quote author
--path an image path

If none are entered, a random meme is generated.

This file can be run by typing meme.py in the command line, after which a new image
file can be found in a static folder.

### app.py
This uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.
This module has same function for making the meme as the meme.py module - finding
images and texts and making the meme. It then uses the requests package to fetch
an image from a user submitted URL.

The app can be run by typing app.py in the command line.

#### Dependencies
Dependencies can be found in requirements.txt
