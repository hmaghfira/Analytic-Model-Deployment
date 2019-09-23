import requests

# URL
url = 'http://localhost:5000/api'


# Change the value of experience that you want to test
r = requests.post(url,json={"LIMIT_BAL":30000,
                            "PAY_1":0,
                            "AGE":22,
                            "EDUCATION":2,
                            "SEX":1})
print(r.json())