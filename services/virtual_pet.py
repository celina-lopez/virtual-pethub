import requests
import os
from dotenv import load_dotenv

def points_to_pet(points):
  if points == 0:
    return "dead"
  elif points == 1:
    return "freak"
  elif points == 2:
    return "whine"
  elif points == 3:
    return "sleep"
  elif points < 6:
    return "happy"
  else:
    return "dancing"

def points_to_quote(points):
  if points == 0:
    return "oops... looks like you need a commit"
  elif points < 3:
    return "pull request, quick!"
  elif points == 3:
    return "the pet is a lil tired"
  else:
    return "keep up the good work!"


def fetch_info(username):
  # load_dotenv()
  accessToken = "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"

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
  last_contributions = data['contributionsCollection']['contributionCalendar']['weeks'][-2:]
  contribution_days = last_contributions[0]["contributionDays"] + last_contributions[1]["contributionDays"][:-1]
  contribution_days.reverse()
  points = 0
  recent_contribution_count = 0
  for i in range(7):
    if contribution_days[i]['contributionCount']:
      recent_contribution_count += contribution_days[i]['contributionCount']
      points+= 1
    
  return {
    "mood": points_to_pet(points),
    "total_contributions": recent_contribution_count,
    "quote": points_to_quote(points),
    "weeks": data['contributionsCollection']['contributionCalendar']['weeks'],
  }

