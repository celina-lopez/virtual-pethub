import requests

# TODO: average commits per week github 

color_theme = {
  "blue": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#c5cae9",
    '#40c463': "#7986cb",
    '#30a14e': "#3949ab",
    '#216e39': "#1a237e",
  },
  "black": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#c5cae9",
    '#40c463': "#7986cb",
    '#30a14e': "#3949ab",
    '#216e39': "#1a237e",
  },
  "mermaid": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#6dc5fb",
    '#40c463': "#f6f68c",
    '#30a14e': "#8affa4",
    '#216e39': "#f283d1",
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
  "rainbow": {
    "#ebedf0": "#ebedf0",
    '#9be9a8': "#6dc5fb",
    '#40c463': "#f6f68c",
    '#30a14e': "#8affa4",
    '#216e39': "#f283d1",
  },
  # "retro": {
  #   "#ebedf0": "#ebedf0",
  #   '#9be9a8': "#6dc5fb",
  #   '#40c463': "#f6f68c",
  #   '#30a14e': "#8affa4",
  #   '#216e39': "#f283d1",
  # },
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

themes = color_theme.keys()

display_themes = {
  "babyblue": "baby blue",
  "black": "black",
  "blue" : "blue",
  "comic": "comic",
  "donut": "donut",
  "flower": "flower",
  "green": "green",
  "love": "love",
  "mermaid": "mermaid",
  "pink": "pink",
  "rainbow": "rainbow",
  # "retro": "retro",
  "sparklegreen": "sparkley green",
  "sparklepink": "sparkley pink",
  "sparklered": "sparkley red",
  "white": "white",
  "whitepink": "white pink",
  "yellow": "yellow",
}

pets = [
  # "mametchi",
  "kurupoyotchi",
  "kurupoyotchi_pink",
  "kurupoyotchi_blue",
  "hanbunkotchi",
  "mokumokutchi",
  "ripputchi",
  "yumehotchi",
]

def get_pet(pet):
  if pet in pets:
    return pet
  else: 
    return pets[0]

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
  accessToken = "access_token"

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

def generate_header(default_color, username):
  return """<svg xmlns="http://www.w3.org/2000/svg" width="300" height="50" fill="none" role="img" aria-labelledby="descId">
        <style>
          .header {{
            font: 600 18px "Courier New", Courier, monospace,  Ubuntu, "Helvetica Neue", Sans-Serif;
            fill: {0};
            animation: fadeInAnimation 0.8s ease-in-out forwards;
          }}
          @supports(-moz-appearance: auto) {{
            /* Selector detects Firefox */
            .header {{ font-size: 15.5px; }}
          }}
          /* Animations */
          @keyframes fadeInAnimation {{
            from {{
              opacity: 0;
            }}
            to {{
              opacity: 1;
            }}
          }}
        </style>
        <g data-testid="card-title" transform="translate(0, 15)">
          <text class="header"  x="50%" dominant-baseline="middle" text-anchor="middle" data-testid="header">{1}'s</text>
        </g>
        <g data-testid="card-title" transform="translate(0, 35)">
          <text class="header"  x="50%" dominant-baseline="middle" text-anchor="middle" >Virtual Pet</text>
        </g>
      </svg>
    """.format(default_color, username)



def generate_contribution_count(total_contributions):
  return """<svg xmlns="http://www.w3.org/2000/svg" width="300" height="30" fill="none" role="img" aria-labelledby="descId">
        <style>
          .stat {{
            font: 600 14px "Courier New", Courier, monospace, Ubuntu, "Helvetica Neue", Sans-Serif; fill: #434d58;
          }}
        
          @supports(-moz-appearance: auto) {{
          /* Selector detects Firefox */
            .stat {{ font-size:12px; }}
          }}
          .stagger {{
            opacity: 0;
            animation: fadeInAnimation 0.3s ease-in-out forwards;
          }}
          .bold {{ font-weight: 700 }}
          /* Animations */
          @keyframes fadeInAnimation {{
            from {{
              opacity: 0;
            }}
            to {{
              opacity: 1;
            }}
          }}
        </style>
        <g class="stagger" style="animation-delay: 450ms">
          <text class="stat bold" x="50%" dominant-baseline="middle" text-anchor="middle"  y="12.5">{0} recent contributions</text>
        </g>
      </svg>
    """.format(total_contributions)


def generate_file_response(pet, username, theme):
  mood = fetch_info(username)["mood"]
  if mood == "dead":
    return "static/%s-%s.gif" % (mood, get_theme(theme))
  else:
    return "static/%s/%s-%s.gif" % (get_pet(pet), mood, get_theme(theme))