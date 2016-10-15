from lxml import html
import requests
import json

class get_detail(object):
    def __init__(self,id):
        self.id = id
    def return_detail(self):
        api_key='a7117cb7dc7f8b768ec323b949e752dd'
        response = []
        page = requests.get('http://food2fork.com/api/get?key='+api_key+'&rId='+str(self.id))
        parsed = json.loads(page.text)
        publisher = parsed['recipe']['publisher']
        print parsed['recipe']['publisher']
        if (publisher == "All Recipes"):
    		tag = '//span[@class="recipe-directions__list--item"]/text()'
    	elif (publisher == "Back to Her Roots"):
    		tag = '//li[@class="instruction"]/text()'
    	elif (publisher == "BBC Food"):
    		tag = '//p[@class="recipe-method__list-item-text"]/text()'
    	elif (publisher == "Bon Appetit"):
    		tag = '//div[@class="text" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Closet Cooking"):
    		tag = '//li[@itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Cookin Canuck"):
    		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Epicurious"):
    		tag = '//li[@class="preparation-step"]/text()'
    	elif (publisher == "Epicurious"):
    		tag = '//li[@class="preparation-step"]/text()'
    	elif (publisher == "Food Republic"):
    		tag = '//span[@itemprop="recipeInstructions"]/ol/li/text()'
    	elif (publisher == "Framed Cooks"):
    		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Healthy Delicious"):
    		tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
    	elif (publisher == "Jamie Oliver"):
    		tag = '//ol[@class="recipeSteps"]/li/text()'
    	elif (publisher == "Lisa's Kitchen"):
    		tag = '//li[@itemprop="recipeInstructions"]/p/text()'
        elif (publisher == "My Baking Addiction"):
            tag = '//span[@itemprop="recipeInstructions"]/ol/li/text()'
        elif (publisher == "Panini Happy"):
            tag = '//li[@class="instruction"]/text()'
        elif (publisher == "PBS Food"):
            tag = '//ol[@class="instructions"]/li/span[@class="txt"]/text()'
        elif (publisher == "Pillsbury Baking"):
            tag = '//ul[@itemprop="recipeInstructions"]/li/text()'
        elif (publisher == "Real Simple"):
            tag = '//section[@class="directions recipe-info-section" and @itemprop="recipeInstructions"]/div/ol/li/text()'
        elif (publisher == "Two Peas and Their Pod"):
            tag = '//div[@class="instructions" and @itemprop="recipeInstructions"]/p/text()'
        elif (publisher == "Vintage Mixer"):
            tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
        elif (publisher == "What's Gaby Cooking" | publisher == "Whats Gaby Cooking"):
            tag = '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'
        else:
    		tag = 404

        if (tag == 404):
            response = json.dumps({'Status':0,'Direction':'NULL','Ingredients':'NULL'},sort_keys=False,separators=(',',':'))
            return str(response).replace("'",'')
        ingredients = parsed['recipe']['ingredients']
        # print ingredients
        url = parsed['recipe']['source_url']
        page1 = requests.get(url)
        #print page1.text
        tree = html.fromstring(page1.content)
        directions = tree.xpath(tag)
        response = json.dumps({'Status':1,'Direction':directions,'Ingredients':ingredients},sort_keys=False,separators=(',',':'))
        return str(response).replace("'",'')

if __name__ == '__main__':
    obj = get_detail("55c5af")
    obj.return_detail()
