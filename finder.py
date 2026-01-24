import requests
get_platform=input("platform: ")
get_username=input("username: ")
url=f"https://api.{get_platform}.com/users/{get_username}"
def code():
    ans=requests.get(url)

    if ans.status_code==200:
        data=ans.json()
        print("=== User Info ===")
        print("Name:", data.get("name"))
        print("Username:", data.get("login") or data.get("username"))
        print("Bio:", data.get("bio"))
        print("Followers:", data.get("followers"))
        print("Following:", data.get("following"))
        print("Profile URL:", data.get("html_url"))
        print("=================")
    else:
        print(f"code failed{ans.status_code}")

code()