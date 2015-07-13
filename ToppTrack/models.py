import datetime
from flask import url_for
from ToppTrack import db

class Seed(db.Document):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	genus = db.StringField(max_length=255, required=True)
	species = db.StringField(max_length=255, required=True)
	line = db.StringField(required=True)
	comments = db.ListField(db.EmbeddedDocumentField('Comment'))

	def get_absolute_url(self):
		return url_for('post', kwargs={"slug": self.slug})

	def __unicode__(self):
		return self.title

	meta = {
		'allow_inheritance': True,
		'indexes': ['-created_at', 'slug'],
		'ordering': ['-created_at']
	}

