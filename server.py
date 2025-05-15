from flask import request, Flask, render_template
from datetime import datetime, timedelta
import requests

API_KEY = "api key"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    current_date = datetime.now()
    one_month_ago = current_date - timedelta(days=31)
    today = current_date.date()
    if request.method == 'POST':
        # making it optional what params to add, topic and pageSize are required but pageSize has a default of 100
        topic = request.form['topic']
        params = {
            "sortBy": request.form['sort-by'],
            "language": request.form['language'],
            "searchIn": request.form['searchIn'],
            "pageSize": request.form['pageSize'],
            "from": request.form['from'],
            "to": request.form['to']
        }
        url_params = ""
        for param in params:
            if params[param] != 'none':
                url_params += f"&{param}={params[param]}"
        print(url_params)
        url = f"https://newsapi.org/v2/everything?q={topic}{url_params}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        return render_template('news.html', articles=articles)
    return render_template('index.html', from_date=one_month_ago, to_date=today)

if __name__ == '__main__':
    app.run(debug=True)
