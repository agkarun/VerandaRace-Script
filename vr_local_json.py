import json
import requests
# Opening JSON file
json_file = open('C:\\Users\Karun\Desktop\VR\json12.json',encoding="utf-8") 
data = json.load(json_file)
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
