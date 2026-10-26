import requests
from ui import Input
def get_data():
    in_put = Input()
    params = in_put.params
    amount = params["num"]
    category = params["cat"]
    difficulty = (params["level"]).lower()
    difficulty = difficulty.lower()
    if category == 0:
        pass
    else:
        category += 8
    BASE_URL = "https://opentdb.com/api.php"
    url = f"{BASE_URL}?amount={amount}&category={category}&difficulty={difficulty}&type=boolean"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(data["results"])
    return data["results"]