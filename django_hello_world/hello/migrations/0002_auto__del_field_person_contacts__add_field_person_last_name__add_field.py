# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.contacts'
        db.delete_column('hello_person', 'contacts')

        # Adding field 'Person.last_name'
        db.add_column('hello_person', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Person.email'
        db.add_column('hello_person', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)

        # Adding field 'Person.jabber'
        db.add_column('hello_person', 'jabber',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Person.skype'
        db.add_column('hello_person', 'skype',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Person.other_contacts'
        db.add_column('hello_person', 'other_contacts',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Person.contacts'
        db.add_column('hello_person', 'contacts',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Person.last_name'
        db.delete_column('hello_person', 'last_name')

        # Deleting field 'Person.email'
        db.delete_column('hello_person', 'email')

        # Deleting field 'Person.jabber'
        db.delete_column('hello_person', 'jabber')

        # Deleting field 'Person.skype'
        db.delete_column('hello_person', 'skype')

        # Deleting field 'Person.other_contacts'
        db.delete_column('hello_person', 'other_contacts')


    models = {
        'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hello']