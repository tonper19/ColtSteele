"""Random user generator.

Found this while watching a Brad Traversy video on 
how to setup Python extension on VS Code.
Check Arepl extension in VSCode.
"""
import requests

def rand(url="https://randomuser.me/api/?results=10"):
    """[summary]
    
    Keyword Arguments:
        url {str} -- [description] (default: {"https://randomuser.me/api/?results=10"})
    
    Returns:
        [type] -- [description]
    """
    response = requests.get(url)
    data = response.json()

    for user in data["results"]:
        print(user["name"]["last"])
    
    return data

if __name__ == "__main__":
    print(rand())
