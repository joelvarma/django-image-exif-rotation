from __future__ import unicode_literals

import os
from django.utils.text import slugify

from django.conf.global_settings import MEDIA_ROOT
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image, ExifTags

from django.db.models.signals import pre_save

from jsmsite.settings import BASE_DIR


def upload_path(instance,filename):
    print "id",instance.id
    return '{0}/{1}'.format("disforum", filename)

class Post(models.Model):
    title=models.CharField(max_length=1201)
    slugf=models.SlugField(unique=True)

    content=models.TextField(max_length=1230)

    fimage=models.ImageField(upload_to=upload_path,null=True,blank=True)


    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postdetail",kwargs={"id": self.id})
        #return "/posts/%s" %(self.id)

def rotate_image(filepath):
  try:
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    image.save(filepath)
    image.close()
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass

@receiver(post_save, sender=Post, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):
  if instance.fimage:

    fullpath = os.path.join(os.path.dirname(BASE_DIR)) + instance.fimage.url
    rotate_image(fullpath)


def pre_save_post_receiver(sender,instance,*args,**kwargs):
    slugf=slugify(instance.title)
    exists=Post.objects.filter(slugf=slugf).exists()
    if exists:
        print instance.id
        slugf="%s-%s"%(slugf,instance.id)

    instance.slugf=slugf



pre_save.connect(pre_save_post_receiver,sender=Post)
