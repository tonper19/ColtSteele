"""Random user generator.

Found this while watching a Brad Traversy video on 
how to setup Python extension on VS Code.
Check Arepl extension in VSCode.
"""
import requests

response = requests.get("https://randomuser.me/api/?results=10")
data = response.json()

for user in data["results"]:
    print(user["name"]["last"])
