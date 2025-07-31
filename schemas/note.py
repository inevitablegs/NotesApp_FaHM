def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "no": item["no"],
        "title": item["title"],
        "desc": item["desc"],
        "imp": item["imp"]
    }
    
    
def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]