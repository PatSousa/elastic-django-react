# import datetime
# from haystack import indexes
# from .models import Note


# class NoteIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     author = indexes.CharField(model_attr='author')
#     pub_date = indexes.DateTimeField(model_attr='pub_date')

#     def get_model(self):
#         return Note
    
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is required"""
#         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


data = {
    "settings": {
        "number_of_shards": 4,
        "number_of_replicas": 1
    },
    "mappings": {
        "note": {
            "properties": {
                "title": { "type": "string", "boost": 4 },
                "text": { "type": "string", "boost": 2 },
                "author": { "type": "string" }
            }
        }
    }
}

import json, requests
response = requests.put('http://127.0.0.1:9200/my_index/', data=json.dumps(data))
print response.text