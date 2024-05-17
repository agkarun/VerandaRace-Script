import json
import requests
my_cookies = dict(Cookie='_gcl_au=1.1.2005246705.1690630961; _ga_SPJZTSE1QC=GS1.1.1690630962.1.0.1690630971.51.0.0;\
                  _ga=GA1.2.517277200.1690630963; _uetsid=07a04bf02e0511ee9abef73986177ea6; _uetvid=07a063b02e0511eea27cef6f601a6533;\
                  _gid=GA1.2.1122761941.1690630969; _ga_0CWXW06XG8=GS1.2.1690630970.1.0.1690630970.60.0.0; \
                  csrftoken=c7J6o1SloOrsgTbjWTwJT2kFKejRTEVqyUb95SubG1Zf2sUBbOpurmEJa0Jr3TOd; sessionid=kbuuoyjpg9sba36xbnvamvh1ppjlcfqj')
jsonurl='https://360.verandalearning.com/api/v2.4/courses/54/contents/?page=4'
json_response = requests.get(jsonurl,cookies=my_cookies)
data = json_response.json()
attachments=data['results']['attachments']
for attachment in attachments:
        try:
                url=(attachment['attachment_url'])
                filename=str(attachment['title']+attachment['description'])\
                        .replace('<p>','').replace('</p>','').replace('\r','').replace('\n','')
                response = requests.get(url)
                with open(filename.replace('  ','',)+'.pdf','wb') as f:
                        f.write(response.content)
                        print('Downloaded===>'+filename)
        except:
                print('Exeption===>'+filename)
                
f.close()
