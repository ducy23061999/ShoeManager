from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

def getShoeWithMax(shoes):
    maxItems = []
    for i in range(0, 12):
        if i < len(shoes):
            maxItems.append(shoes[i])
        else:
            break
    return maxItems

def serialize(obj):
    return serializers.serialize('json', [ obj, ])
def parseOne(obj):
    objcs = serializers.deserialize('json', obj)
    for obj in objcs:
        return obj.object
    return None
def parseMany(obj):
    def convert(x):
        return x.object
    rawObjects = serializers.deserialize('json', obj)
    listObject = map(convert, rawObjects)
    return rawObjects