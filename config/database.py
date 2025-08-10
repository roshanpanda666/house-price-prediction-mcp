from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

username=os.getenv("USERNAME")
password=os.getenv("PASSWORD")

print(username,password)

mongo_uri=f"mongodb+srv://{username}:{password}@cluster0.x3ytifd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client=MongoClient(mongo_uri)

db=client["MCP"]
collection=db["datas"]

