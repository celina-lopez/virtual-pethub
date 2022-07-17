import os
import mistune
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from services import virtual_pet

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/favicon.ico")
async def favicon(): return FileResponse('./static/favicon.ico')

templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False)
async def index(request: Request):
    with open('README.md', 'r') as readme:
        readme_content = readme.read()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "readme": mistune.html(readme_content)
        })


@app.get("/{username}")
async def upload(username, request: Request, theme: str = "normal"):
  load_dotenv()
  data = virtual_pet.fetch_info(username)

  return templates.TemplateResponse("virtual_pet.html", {
            "request": request,
            "mood": data['mood'],
            "theme": theme,
            "username": username,
            "quote": data['quote'],
            "total_contributions": data['total_contributions'],
            "weeks": data["weeks"],
        })
   
if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', "8000")))
