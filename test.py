from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp()

model = app.models.get('food-items-v1.0')

image = ClImage(url='http://www.bolas.co.in/resource/uploads/pages/about-cashew/cashew-kernel_21792013.jpg')

# print(model.predict([image2]))
# image = ClImage(url='self.url')
# print image
d1 = model.predict([image])
# print d1
d2 = d1[u'outputs'][0][u'data'][u'concepts'][0][u'name']
print d2
