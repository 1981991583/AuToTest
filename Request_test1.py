import requests
import json

url="http://frontgatewayv4-cquat.yuantutech.com/frontgateway/api/patient-info/query-by-account"

headers={'Content-Type':"application/json"}
body={
    "corpId": 9999,
    "deviceIp": "192.9.14.249",
    "deviceNo": "ZZJ001",
    "operId": "ZZJ001",
    "terminalNo": "ZZJ001",
    "userAccountId": "11f97803f4d141e985a999415785929f"
}
r=requests.post(url,data=json.dumps(body),headers=headers)
result=r.json()['data']['patientName']
print(result)
