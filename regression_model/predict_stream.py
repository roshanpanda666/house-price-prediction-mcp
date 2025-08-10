from config.database import collection

def start_data_monitor(callback_function):
    """
    Starts monitoring the MongoDB collection for new inserts and 
    triggers the given callback function when new data is inserted.
    
    :param callback_function: function to call with new data
    """
    try:
        print("⏳ Starting to monitor MongoDB for new inserts...")
        with collection.watch([{"$match": {"operationType": "insert"}}]) as stream:
            for change in stream:
                new_data = change["fullDocument"]
                print("📦 New data inserted! Triggering callback...")
                callback_function(new_data)
    except Exception as e:
        print(f"❌ Error in data monitor: {e}")


