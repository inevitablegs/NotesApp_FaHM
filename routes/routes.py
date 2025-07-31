from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    docList = []
    docs = conn.notes.notes.find({})
    for doc in docs:
        docList.append({
            "id": str(doc["_id"]),
            "no": doc.get("no", 0),  # Using .get() with default value
            "title": doc.get("title", ""),
            "desc": doc.get("desc", ""),
            "imp": doc.get("imp", False)  # Default to False if not present
        })
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"request": request, "docList": docList}
    )

@note.post("/")
async def create_note(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["imp"] = "important" in formDict and formDict["important"] == "on"
    formDict.pop("important", None)
    conn.notes.notes.insert_one(formDict)
    return {"Success": True}