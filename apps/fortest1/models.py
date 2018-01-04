from __future__ import unicode_literals

from django.db import models

# Create your models here.


from mongoengine import *


connect('MyDjango')


class test(Document):
    name=StringField()
    tags=ListField()
    age=IntField()
    address=StringField()



    meta={
        'collection':'MyDjango_col'
    }


# thisclass=test()
# thisclass.name='李四'
# thisclass.age=21
# thisclass.tags=['男生','宅男','卡通迷']
# thisclass.address='北京市'
# thisclass.save()
# print(thisclass.name)