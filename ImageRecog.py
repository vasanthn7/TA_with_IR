from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

class get_ing(object):
    def __init__(self,url):
        self.url = url
    def return_ing(self):
        app = ClarifaiApp()
        model = app.models.get('food-items-v1.0')
        image = ClImage(url=self.url)
        d1 = model.predict([image])
        d2 = d1[u'outputs'][0][u'data'][u'concepts'][0][u'name']
        return d2

if __name__ == '__main__':
    obj = get_ing("http://www.songawayfarm.com/uploads/8/8/3/2/8832016/4125371_orig.jpg")
    print obj.return_ing()





# app = ClarifaiApp()
# model = app.models.get('food-items-v1.0')
# image = ClImage(url='http://www.bolas.co.in/resource/uploads/pages/about-cashew/cashew-kernel_21792013.jpg')
# d1 = model.predict([image])
# d2 = d1[u'outputs'][0][u'data'][u'concepts'][0][u'name']
# print d2
