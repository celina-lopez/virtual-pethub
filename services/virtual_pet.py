import requests

color_theme = {
  "blue": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#c5cae9",
    '#40c463': "#7986cb",
    '#30a14e': "#3949ab",
    '#216e39': "#1a237e",
  },
  "pink": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#6dc5fb",
    '#40c463': "#f6f68c",
    '#30a14e': "#8affa4",
    '#216e39': "#f283d1",
  },
  "github": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#9be9a8",
    '#40c463': "#40c463",
    '#30a14e': "#30a14e",
    '#216e39': "#216e39",
  },
  "babyblue": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#b3e5fc",
    '#40c463': "#4fc3f7",
    '#30a14e': "#039be5",
    '#216e39': "#01579b",
  },
  "comic": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#b3e5fc",
    '#40c463': "#4fc3f7",
    '#30a14e': "#039be5",
    '#216e39': "#01579b",
  },
  "donut": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#6dc5fb",
    '#40c463': "#f6f68c",
    '#30a14e': "#8affa4",
    '#216e39': "#f283d1",
  },
  "flower": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#fed800",
    '#40c463': "#ff6f01",
    '#30a14e': "#fd2f24",
    '#216e39': "#811d5e",
  },
  "green": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#9be9a8",
    '#40c463': "#40c463",
    '#30a14e': "#30a14e",
    '#216e39': "#216e39",
  },
  "love": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#ffcdd2",
    '#40c463': "#e57373",
    '#30a14e': "#e53935",
    '#216e39': "#b71c1c",
  },
  "retro": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#6dc5fb",
    '#40c463': "#f6f68c",
    '#30a14e': "#8affa4",
    '#216e39': "#f283d1",
  },
  "sparklegreen": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#f0f4c3",
    '#40c463': "#dce775",
    '#30a14e': "#c0ca33",
    '#216e39': "#827717",
  },
  "sparklepink": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#6dc5fb",
    '#40c463': "#f6f68c",
    '#30a14e': "#8affa4",
    '#216e39': "#f283d1",
  },
  "sparklered": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#ffcdd2",
    '#40c463': "#e57373",
    '#30a14e': "#e53935",
    '#216e39': "#b71c1c",
  },
  "white": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#e0e0e0",
    '#40c463': "#9e9e9e",
    '#30a14e': "#616161",
    '#216e39': "#212121",
  },
  "whitepink": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#ffcdd2",
    '#40c463': "#e57373",
    '#30a14e': "#e53935",
    '#216e39': "#b71c1c",
  },
  "yellow": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#eae374",
    '#40c463': "#f9d62e",
    '#30a14e': "#fc913a",
    '#216e39': "#ff4e50",
  },
}
themes = [
  "babyblue",
  "blue",
  "comic",
  "donut",
  "flower",
  "green",
  "love",
  "pink",
  "retro",
  "sparklegreen",
  "sparklepink",
  "sparklered",
  "white",
  "whitepink",
  "yellow",
]

def get_color_theme(theme):
  if theme in themes:
    return color_theme[theme]
  else: 
    return color_theme["github"]


def get_theme(theme):
  if theme in themes:
    return theme
  else:
    return "pink"


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
  accessToken = "Access Code"

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

