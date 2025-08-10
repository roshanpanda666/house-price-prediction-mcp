from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os

load_dotenv(override=True)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def push_predictions_to_db():
    # 📂 Read predicted.txt
    try:
        with open("virtualfile/predicted.txt", "r") as file:
            predictions = json.load(file)
    except FileNotFoundError:
        print("❌ predicted.txt not found! Make sure the prediction step ran.")
        return
    except json.JSONDecodeError:
        print("❌ JSON decode error! Check the structure of predicted.txt")
        return

    # 🔗 Connect to MongoDB
    try:
        client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.x3ytifd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client["MCP"]
        collection = db["predicted-data"]

        # 📤 Insert all predictions
        if predictions:
            collection.insert_many(predictions)
            print("✅ Predictions pushed to MongoDB Atlas!")
        else:
            print("⚠️ No predictions to insert.")
    except Exception as e:
        print(f"❌ MongoDB Error: {e}")

if __name__ == "__main__":
    push_predictions_to_db()
