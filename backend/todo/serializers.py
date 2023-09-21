from rest_framework import serializers
from .models import Todo


# Serializers in Django REST Framework are responsible for converting objects into data types (JSON, XML) understandable by javascript and front-end frameworks. 
# Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. 
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','completed')

# TodoSerializer is a subclass of serializers.ModelSerializer.
# The Meta class inside the serializer defines the model to be serialized (Todo) and the fields to be included in the serialized representation
# You can use this serializer in your views to serialize data