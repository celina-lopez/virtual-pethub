import os
import mistune
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from services import virtual_pet
import random

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
            "readme": mistune.html(readme_content),
            "themes": virtual_pet.display_themes,
            "pets": virtual_pet.pets,
        })


@app.get("/{username}")
async def upload(username, request: Request, theme: str = "pink", pet: str = "hanbunkotchi"):
  load_dotenv()
  data = virtual_pet.fetch_info(username)

  return templates.TemplateResponse("virtual_pet.html", {
            "request": request,
            "mood": data['mood'],
            "theme": virtual_pet.get_theme(theme),
            "pet": virtual_pet.get_pet(pet),
            "username": username,
            "quote": data['quote'],
            "total_contributions": data['total_contributions'],
            "weeks": data["weeks"],
            "colors": virtual_pet.get_color_theme(theme),
        })

@app.get("/{username}/{pet}/{theme}.gif")
def get_image(username, pet, theme):
  gif = virtual_pet.generate_file_response(pet, username, theme)
  headers = {"Cache-Control:": "no-cache"}
  return FileResponse(gif, headers=headers)


@app.get("/{username}/{theme}/header.svg")
def get_image(username, theme):
  content = virtual_pet.generate_header(virtual_pet.get_color_theme(theme)["#216e39"], username)
  return Response(content=content, media_type="image/svg+xml")

@app.get("/{username}/contributions.svg")
def get_image(username):
  data = virtual_pet.fetch_info(username)
  content = virtual_pet.generate_contribution_count(data['total_contributions'])
  headers = {"Cache-Control:": "no-cache"}
  return Response(content=content, media_type="image/svg+xml", headers=headers)


   
if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', "8000")))
