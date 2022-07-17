import requests
import os
from dotenv import load_dotenv

def points_to_pet(points):
  if points == 0:
    return "dead.png"
  elif points == 1:
    return "freak.webp"
  elif points == 2:
    return "whine.webp"
  elif points == 3:
    return "sleep.gif"
  elif points < 6:
    return "happy.webp"
  else:
    return "dancing.webp"


def fetch_info(username):
  load_dotenv()
  accessToken = os.getenv('GITHUB_ACCESS_TOKEN')

  endpoint = "https://api.github.com/graphql"
  headers = {"Authorization": f"Bearer {accessToken}"}

  query = """query {{
    user(login: "{0}") {{
      name
      avatarUrl
      contributionsCollection {{
        contributionCalendar {{
          totalContributions
          weeks {{
            contributionDays {{
              contributionCount
              date
              color
            }}
            firstDay
          }}
        }}
      }}
    }}
  }}""".format(username)

  r = requests.post(endpoint, json={"query": query}, headers=headers)
  data = r.json()['data']['user']
  total_contributions = data['contributionsCollection']['contributionCalendar']['totalContributions']
  last_contributions = data['contributionsCollection']['contributionCalendar']['weeks'][-2:]
  contribution_days = last_contributions[0]["contributionDays"] + last_contributions[1]["contributionDays"][:-1]
  contribution_days.reverse()
  points = 0
  for i in range(7):
    if contribution_days[i]['contributionCount']:
      points+= 1
    
  return {
    "total_contributions": total_contributions,
    "mood": points_to_pet(points),
    "weeks": data['contributionsCollection']['contributionCalendar']['weeks'],
  }

