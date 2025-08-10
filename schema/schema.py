def individual_serial(thing)->dict:
    return{
        "id": str(thing["_id"]),
        "house":str(thing["house"]),
        "price1": str(thing["price1"]),
        "price2": str(thing["price2"]),
        "price3": str(thing["price3"]),
        "year1": str(thing["year1"]),
        "year2": str(thing["year2"]),
        "year3": str(thing["year3"]),
        "area": str(thing["area"]),
    }

def list_serial(things)->list:
    return[individual_serial(thing)for thing in things]
