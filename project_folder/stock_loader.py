# stock_loader.py

import pandas as pd
import mplfinance as mpf
import os

def load_and_plot_stock(stock_name):
    folder = os.path.join('static', 'archive(2)')
    file_path = os.path.join(folder, f'{stock_name}.csv')
    
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date column is datetime
        df.set_index('Date', inplace=True)       # Set Date as index

        # Save the plot
        plot_save_path = os.path.join('static', f'{stock_name}.png')
        mpf.plot(
            df,
            type='candle',
            style='yahoo',
            title=stock_name,
            ylabel='Price',
            savefig=plot_save_path
        )
        return True, f'{stock_name}.png'
    except FileNotFoundError:
        print(f"File not found for {stock_name}")
        return False, None
    except Exception as e:
        print(f"Error loading/plotting {stock_name}: {e}")
        return False, None
