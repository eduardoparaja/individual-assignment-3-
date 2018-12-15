import requests

def get_repository_info(username):
    url = "https://api.github.com/users/{}/repos".format(username)
    
    user_repositories = requests.get(url).json()
    repositories = []
    
    for repo in user_repositories:
        repo_info = {"Repository":repo["name"],
                     "Language":repo["language"],
                     "Stars":repo["stargazers_count"],
                     "url":repo["url"]
                     }
        repositories.append(repo_info)
    return repositories
    
get_repository_info("eduardoparaja")