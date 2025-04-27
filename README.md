# Live_Stock_preview



<h1>🚀 Stock Market Candle Chart Web App</h1>

This is a Flask web application that allows users to view live stock market candlestick charts for various stocks in the Nifty 50 index. The project dynamically loads historical stock data from multiple CSV files and generates interactive candlestick charts using the mplfinance library.

The web application serves the charts using Flask, and users can easily view and interact with the data on a beautifully styled web interface.

<h2>📈 Features</h2>
Interactive Candlestick Charts: View detailed candlestick charts for different Nifty 50 stocks (e.g., RELIANCE, INFY, TCS).

Historical Data: The app loads stock data from multiple CSV files, which contain historical price data for each stock.

Flask Backend: The backend of the web app is powered by Flask, which processes data and renders charts dynamically.

mplfinance Library: Utilizes mplfinance to generate interactive and high-quality candlestick charts.

Base64 Encoding: The generated charts are encoded in Base64 format and directly embedded into the web page for fast rendering without needing to save images to disk.

<h2>🛠 Technologies Used</h2>
Python:

<bold>Flask</bold> (for the web server)

Pandas (for data handling)

mplfinance (for generating stock charts)

Base64 (for embedding charts into HTML)

HTML/CSS:

Basic web page structure and styling

GitHub:

Version control and repository hosting

📂 Project Structure
graphql
Copy code
project_folder/
├── static/
│   ├── nifty_fifty_folder/   # Folder containing all Nifty 50 stock CSV files
│   ├── style.css             # Custom CSS for frontend
├── templates/
│   ├── index.html            # HTML template to render the stock chart
├── app.py                    # Flask backend to serve the application
├── stock_loader.py           # Python script to load stock data from CSV files


🔧 How It Works
The app reads multiple CSV files from the static/nifty_fifty_folder/ directory.

Each CSV file contains stock data, including dates and stock prices for different companies in the Nifty 50 index.

When a user visits the homepage (/), Flask loads the data and generates a candlestick chart for a default stock (currently RELIANCE).

The generated chart is returned as a Base64 image and displayed in the user's browser.

You can easily extend the app to allow users to select different stocks dynamically or add more features, such as live data fetching.

🚧 Future Improvements
Stock Selection: Add a dropdown menu to let users select different stocks from the Nifty 50 index.

Live Data: Integrate with APIs (e.g., Yahoo Finance or Alpha Vantage) to fetch live stock data instead of relying on static CSV files.

Modern UI: Improve the user interface by adding modern web design frameworks like Bootstrap or Tailwind CSS.

Chart Customization: Allow users to adjust chart parameters like time range, chart type, and indicators.

Performance Enhancements: Implement caching or data pre-fetching to speed up loading times for large datasets.

💡 Contributing
Feel free to contribute to this project! You can:

Submit bug reports or feature requests.

Improve the UI/UX.

Add new features or enhancements.

Improve the documentation.

🚀 Demo:
If you'd like to see a demo of the web app, follow the instructions above to set it up on your local machine. You can also contribute new features or fixes!

🙌 Happy Coding!
