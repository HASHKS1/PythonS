
from flask import Flask, request, jsonify
import short_links

# init the Flask app
app = Flask(__name__)


@app.route('/shorten', methods=['POST'])

def shorten():

    link_key = 'link'
    data = request.get_json()
    print(data)

    if link_key not in data:
        return jsonify({'error': 'No link provided'}), 400
    
    link = data['link']

    try:
        short_link = short_links.shortLink(link)
        return jsonify({'shortened_link': short_link}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)