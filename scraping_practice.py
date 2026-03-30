import requests

response = requests.get("https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/60680")
print(response.status_code)
print(response.text)