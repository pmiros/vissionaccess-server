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
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    content = request.json
    text = content['image']
    # Create an empty list for our results
    results = "helo"

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    im = Image.open(BytesIO(base64.b64decode(text)))
    im.save('image.png', 'PNG')

    results = pytesseract.image_to_string(Image.open("image.png"))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    print(results)
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(image=results)

if __name__ == '__main__':
    app.run(port=int("5000"))
