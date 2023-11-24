from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    amazon_url = request.form['amazon_url']
    flipkart_url = request.form['flipkart_url']

    amazon_data = scrape_amazon(amazon_url)
    flipkart_data = scrape_flipkart(flipkart_url)

    return render_template('result.html', amazon_data=amazon_data, flipkart_data=flipkart_data)

def scrape_amazon(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}

    response = requests.get(url, headers=head)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("span", attrs={'id': 'productTitle'})
        price = soup.find("span", attrs={'class': 'a-price-whole'})

        return {'title': title.text.strip(), 'price': '₹' + price.text.strip()}

    return {'error': f"Failed to retrieve the page. Status code: {response.status_code}"}

def scrape_flipkart(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}

    response = requests.get(url, headers=head)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("span", attrs={'class': 'B_NuCI'})
        price = soup.find("div", attrs={'class': '_30jeq3 _16Jk6d'})

        return {'title': title.text.strip(), 'price': price.text.strip()}

    return {'error': f"Failed to retrieve the page. Status code: {response.status_code}"}

def open_browser():
    # Open the default web browser
    webbrowser.open('http://127.0.0.1:5000/')


if __name__ == '__main__':
    # Create a thread to open the browser
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.start()

    # Run the Flask application in the main thread
    app.run(debug=True, use_reloader=False)
