import requests


# Request QnA API
# for QnA Service access
SubscriptionKey="609b73185db64be0adc1e614b25ec605"
ServiceID="b246d74a-8df6-492f-acd8-a56be53b9563"

def qna_response(query):
    url = "https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/"+ServiceID+"/generateAnswer"
    headers = {
       "Ocp-Apim-Subscription-Key": SubscriptionKey,
       "Content-Types": "application/json"
    }

    payload = {"question":query}
    result = ""
    try:
        response = requests.post(url, data=payload, headers=headers)
        jsonresult = response.json()
        result = jsonresult["answers"][0]["answer"]
    except:
        print(response.status_code, response.reason)

    print(result)
    return result


