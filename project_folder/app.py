# app.py

from flask import Flask, render_template, request
from stock_loader import load_and_plot_stock

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_filename = None
    stock_name = ''
    
    if request.method == 'POST':
        stock_name = request.form.get('stock_name').upper()
        success, filename = load_and_plot_stock(stock_name)
        if success:
            chart_filename = filename

    return render_template('index.html', chart_filename=chart_filename, stock_name=stock_name)

if __name__ == '__main__':
    app.run(debug=True)
