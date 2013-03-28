# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tags'
        db.create_table('post_tags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('post', ['Tags'])

        # Adding model 'Category'
        db.create_table('post_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('post', ['Category'])

        # Adding model 'Post'
        db.create_table('post_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['post.Category'])),
        ))
        db.send_create_signal('post', ['Post'])

        # Adding M2M table for field tags on 'Post'
        db.create_table('post_post_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['post.post'], null=False)),
            ('tags', models.ForeignKey(orm['post.tags'], null=False))
        ))
        db.create_unique('post_post_tags', ['post_id', 'tags_id'])


    def backwards(self, orm):
        # Deleting model 'Tags'
        db.delete_table('post_tags')

        # Deleting model 'Category'
        db.delete_table('post_category')

        # Deleting model 'Post'
        db.delete_table('post_post')

        # Removing M2M table for field tags on 'Post'
        db.delete_table('post_post_tags')


    models = {
        'post.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'post.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['post.Category']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['post.Tags']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'post.tags': {
            'Meta': {'object_name': 'Tags'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['post']