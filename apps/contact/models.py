# encoding: utf-8

from django.db import models

class Contact(models.Model):
    datetime = models.DateTimeField('Publication date', auto_now_add=True)
    author_name = models.CharField('Autor name', max_length = 100)
    email = models.CharField('Email', max_length = 100)
    message = models.CharField('Message', max_length = 100)

    def __unicode__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'

