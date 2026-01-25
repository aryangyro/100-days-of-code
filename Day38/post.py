import requests
from datetime import datetime
user = "aryanpanwar"
tk = "djgklshgkshss"
id = "mutthi"
time = "20260121"

endpoint = f"https://pixe.la//v1/users/{user}/graphs/{id}"

# now = datetime.now().strftime("%Y%m%d")

params = {
    "date": "20260121",
    # "quantity" : "10",
        
}
headers = {
    "X-USER-TOKEN" : tk,  
}

ans = requests.delete(url=endpoint,json=params,headers=headers)
print(ans.text)