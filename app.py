from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_random_quote():
    """Получение случайной цитаты с API"""
    response = requests.get('http://api.quotable.io/random')
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'POST':
        quote = get_random_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)