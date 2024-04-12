from django.db import models

from wagtail.api import APIField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

# Create your models here.
class AboutPage(Page):
    intro = models.CharField(max_length=255)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    api_fields = [
        APIField('title'),
        APIField('intro'),
        APIField('body')
    ]

