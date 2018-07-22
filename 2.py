import argparse
import io
import os

from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/sharat/Ethereum Node-ad7f8d92b54c.json'


def detect_document(path):
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            print('Block Content: {}'.format(block_text))
            print('Block Bounds:\n {}'.format(block.bounding_box))



client = vision.ImageAnnotatorClient()
with io.open('latest.jpg', 'rb') as image_file:
        content = image_file.read()
image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)
document = response.full_text_annotation
print(document.text)





