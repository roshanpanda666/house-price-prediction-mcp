import json
from regression_model.regression_engine import predict_prices

# Get predictions
future_predictions = predict_prices()
print("\n🧾 Returned Predictions List:")
print(future_predictions)

# Convert to JSON-serializable format
converted_predictions = [
    {"year": int(year), "predicted_price": int(price)}
    for year, price in future_predictions
]

# Write to file
with open("virtual/predicted.txt", "w") as f:
    json.dump(converted_predictions, f, indent=4)

print("✅ Predictions saved to predicted.txt in JSON format!")
