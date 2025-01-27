from flask import request, Flask, render_template
import requests

API_KEY = "b7a5e5365379415fb44da1db110c1d02"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        topic = request.form['topic']
        sortBy = request.form['sort-by']
        language = request.form['language']
        searchIn = request.form['searchIn']
        pageSize = request.form['pageSize']
        from_date = request.form['from']
        to_date = request.form['to']
        url = f"https://newsapi.org/v2/everything?q={topic}&sortBy={sortBy}&language={language}&searchIn={searchIn}&pageSize={pageSize}&from={from_date}&to={to_date}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        return render_template('news.html', articles=articles)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)