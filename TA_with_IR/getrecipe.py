from lxml import html
import requests
import json
from validity import valid
# from flask import Flask

class get_recipe(object):
    def __init__(self, list, pg):
        self.list = list
        self.pg = pg
    def return_recipe(self):
        api_key='a7117cb7dc7f8b768ec323b949e752dd'
        # for i in range(len(self.list)):
        #     ingr = ingr+self.list[i]+','
        # ingr = ingr[:-1]
        response = []
        num = 0
        page = requests.get('http://food2fork.com/api/search?key='+api_key+'&q='+self.list+'&page='+str(self.pg))
        parsed = json.loads(page.text)
        count = parsed['count']
        for i in range(0,count):
            if(valid(parsed['recipes'][i]['publisher'])):
                temp  = json.dumps({'title':parsed['recipes'][i]['title'],'id':parsed['recipes'][i]['recipe_id']},separators=(',',':'))
                response.append(temp)
                num=num+1
        return str(response).replace("'",'')

if __name__ == '__main__':
    obj = get_recipe("shredded chicken",1)
    obj.return_recipe()
