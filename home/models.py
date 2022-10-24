from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    """Home page Model"""
    templates = "/home/home_page.html"

    banner_title = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]