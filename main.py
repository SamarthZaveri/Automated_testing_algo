from data_fetcher import fetch_data
from strategy import generate_signals
from backtest import backtest
from ml_model import train_predict
from google_sheets import log_to_sheet
from notifier import send_alert
from utils import logger


if __name__ == "__main__":
    logger.info("Fetching stock data...")
    data = fetch_data()


for stock, df in data.items():
    logger.info(f"Processing {stock}")
    df = generate_signals(df)


trades, final_value = backtest(df)
model, acc = train_predict(df)


log_to_sheet("TradeLog", [stock, str(trades), final_value, acc])
send_alert(f"{stock}: Final Value = {final_value}, Accuracy = {acc:.2f}")


logger.info("Algo Trading Run Complete!")