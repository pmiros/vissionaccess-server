import flask
from flask import request, jsonify
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

from io import BytesIO
import base64


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def api_text():
    #receives the json form POST request
    content = request.json
    text = content['image']
    # Create an empty var for our results
    results = ""

    #receives image and saves it on the server as png
    im = Image.open(BytesIO(base64.b64decode(text)))
    im.save('image.png', 'PNG')
    #using pytesseract and train data to read the message off screen
    results = pytesseract.image_to_string(Image.open("image.png"))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    print(results)
    # Use the jsonify function from Flask to convert our string
    #  to the JSON format.
    return jsonify(image=results)

if __name__ == '__main__':
    app.run(port=int("5000"))
