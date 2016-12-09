import json, requests
from elastic.models import Note
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = ''    
        for p in Note.objects.all():
            data += '{"index": {"_id": "%s"}}\n' % p.pk
            
            # for field in p._meta.fields:
            #     import ipdb ; ipdb.set_trace()
            #     data += json.dumps({ field.name: getattr(p, field.name) })
           
            data += json.dumps({
                "title": p.title,
                "text": p.text,
                "author": p.author.id,
                "pub_date": str(p.pub_date)
            })+'\n'    
        response = requests.put('http://127.0.0.1:9200/my_index/elastic/_bulk', data=data)
        print response.text