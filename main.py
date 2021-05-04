from google.cloud import vision
import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "myFirst.json"

"""Detects document features in an image."""
def detect_document(path):

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    text = ""
    sentences = []

    for page in response.full_text_annotation.pages:
        for block in page.blocks:

            for paragraph in block.paragraphs:
                # print(paragraph)
                s = ""
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    if word_text == "." or word_text == "?":
                        s += word_text
                        print(s)
                        sentences.append(s)
                        text += s + " "
                        s = ""
                    elif word_text == ",":
                        s += word_text
                    else:
                        s += " " + word_text

                print()
                # print("************")

    print(text)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return sentences


def scan_receipt(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts: ")
    # print(type(texts))
    for text in texts:

        # print('\n"{}"'.format(text.description))

        print(text.description)
        if text.description == "  ":
            break
        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #              for vertex in text.bounding_poly.vertices])
        #
        # print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message)
        )

# detect_document("image.jpg")
test = detect_document("image.jpg")
print(test)
# scan_receipt("receipt.jpg")
# scan_receipt("emart.jpeg")
# scan_receipt("lotte2.jpg")