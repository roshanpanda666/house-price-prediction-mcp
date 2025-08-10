import requests
import numpy as np
from sklearn.linear_model import LinearRegression
from tqdm import tqdm
import time
import json
import os
from push_to_predicted_cluster.push import push_predictions_to_db

def predict_prices():
    print("📡 Fetching data from backend...")
    response = requests.get("https://house-price-prediction-mcp.onrender.com/")
    data = response.json()
    print("✅ Data fetched!")

    raw = data[-1]  # latest entry
    house_no = raw.get("house", "Unknown")  # Grab house_no safely

    years = [int(raw["year1"]), int(raw["year2"]), int(raw["year3"])]
    prices = [int(raw["price1"]), int(raw["price2"]), int(raw["price3"])]

    X = np.array(years).reshape(-1, 1)
    y = np.array(prices)

    print("\n⚙️ Training Model...")
    for _ in tqdm(range(100), desc="🔧 Analyzing", ncols=75):
        time.sleep(0.005)

    model = LinearRegression()
    model.fit(X, y)

    last_year = max(years)
    future_years = np.array([last_year + i for i in range(1, 11)]).reshape(-1, 1)
    predicted_prices = []

    print("\n📊 Predicting next 10 years...")
    for year in tqdm(future_years, desc="📈 Predicting", ncols=75):
        time.sleep(0.01)
        price = model.predict(year.reshape(1, -1))[0]
        predicted_prices.append(int(price))

    print("\n📌 Actual Data:")
    for year, price in zip(years, prices):
        print(f"Year: {year} | Price: ₹{price}")

    print("\n🔮 Predicted Prices for Next 10 Years:")
    for year, price in zip(future_years.ravel(), predicted_prices):
        print(f"Year: {year} | Predicted Price: ₹{price}")

    # Prepare JSON with house_no
    predictions_json = [
        {
            "house_no": house_no,
            "year": int(year),
            "predicted_price": int(price)
        }
        for year, price in zip(future_years.ravel(), predicted_prices)
    ]

    # Make sure the directory exists
    os.makedirs("virtualfile", exist_ok=True)

    # Write to predicted.txt
    with open("virtualfile/predicted.txt", "w") as f:
        json.dump(predictions_json, f, indent=4)

    print("✅ Predictions saved to predicted.txt in JSON format!")

    # Push to Mongo cluster
    push_predictions_to_db()

    return predictions_json
