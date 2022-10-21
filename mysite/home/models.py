from django.db import models

from wagtail.models import Page


class HomePage(Page):
    """Home page Model"""
    templates = "/templates/home/home_page.html"

    #banner_title = models.CharField(max_length=100, blank=False, null=True)