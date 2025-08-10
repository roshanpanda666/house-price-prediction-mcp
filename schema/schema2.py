def list_serial(data) -> list:
    return [serialize_doc(doc) for doc in data]

def serialize_doc(doc) -> dict:
    doc["_id"] = str(doc["_id"])
    return doc
