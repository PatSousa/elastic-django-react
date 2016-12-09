# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 15:00
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User
import datetime

# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import migrations, models
from elastic.models import Note

sousa = User.objects.filter(is_superuser=True).first()
today = datetime.datetime.now()

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Note = apps.get_model("elastic", "Note")
    db_alias = schema_editor.connection.alias
    Note.objects.using(db_alias).bulk_create([
        Note(title="Certainly elsewhere", text="Certainly elsewhere my do allowance at. The address farther six hearted hundred towards husband. Are securing off occasion remember daughter replying. Held that feel his see own yet. Strangers ye to he sometimes propriety in. She right plate seven has. Bed who perceive judgment did marianne."),
        Note(title="Parish so enable innate", text="Parish so enable innate in formed missed. Hand two was eat busy fail. Stand smart grave would in so. Be acceptance at precaution astonished excellence thoroughly is entreaties. Who decisively attachment has dispatched. Fruit defer in party me built under first. Forbade him but savings sending ham general. So play do in near park that pain.",), 
       Note(title="Assure polite his", text="Assure polite his really and others figure though. Day age advantages end sufficient eat expression travelling. Of on am father by agreed supply rather either. Own handsome delicate its property mistress her end appetite. Mean are sons too sold nor said. Son share three men power boy you. Now merits wonder effect garret own. ",),
        Note(title="Satisfied conveying", text="Satisfied conveying an dependent contented he gentleman agreeable do be. Warrant private blushes removed an in equally totally if. Delivered dejection necessary objection do mr prevailed. Mr feeling do chiefly cordial in do. Water timed folly right aware if oh truth. Imprudence attachment him his for sympathize. Large above be to means. Dashwood do provided stronger is. But discretion frequently sir the she instrument unaffected admiration everything", ),
        Note(title="May musical arrival", text="May musical arrival beloved luckily adapted him. Shyness mention married son she his started now. Rose if as past near were. To graceful he elegance oh moderate attended entrance pleasure. Vulgar saw fat sudden edward way played either. Thoughts smallest at or peculiar relation breeding produced an. At depart spirit on stairs. She the either are wisdom praise things she before. Be mother itself vanity favour do me of. Begin sex was power joy after had walls miles. ",)
        ])



def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Note = apps.get_model("elastic", "Note")
    db_alias = schema_editor.connection.alias
    Note.objects.using(db_alias).filter(title="Certainly elsewhere").delete()
    Note.objects.using(db_alias).filter(title="Parish so enable innate").delete()
    Note.objects.using(db_alias).filter(title="Assure polite his").delete()
    Note.objects.using(db_alias).filter(title="Satisfied conveying").delete()
    Note.objects.using(db_alias).filter(title="May musical arrival").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('elastic', '0002_auto_20161205_1448'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
