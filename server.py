from flask import request, Flask, render_template
import requests

API_KEY = "b7a5e5365379415fb44da1db110c1d02"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        topic = request.form['topic']
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        print(data)
        return render_template('news.html', topic=topic)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)