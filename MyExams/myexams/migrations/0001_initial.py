# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Student'
        db.create_table(u'myexams_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('enrolled', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'myexams', ['Student'])

        # Adding model 'Teacher'
        db.create_table(u'myexams_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('hired', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'myexams', ['Teacher'])

        # Adding model 'School'
        db.create_table(u'myexams_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'myexams', ['School'])

        # Adding model 'Semester'
        db.create_table(u'myexams_semester', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.DateField')()),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'myexams', ['Semester'])

        # Adding model 'Course'
        db.create_table(u'myexams_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Teacher'])),
            ('semester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Semester'])),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.School'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'myexams', ['Course'])

        # Adding model 'StudentCourses'
        db.create_table(u'myexams_studentcourses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Course'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Student'])),
        ))
        db.send_create_signal(u'myexams', ['StudentCourses'])

        # Adding model 'Exam'
        db.create_table(u'myexams_exam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Course'])),
            ('exam_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateField')()),
            ('return_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'myexams', ['Exam'])

        # Adding model 'Question'
        db.create_table(u'myexams_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Exam'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'myexams', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'myexams_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Question'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'myexams', ['Answer'])

        # Adding model 'ExamsTaken'
        db.create_table(u'myexams_examstaken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Exam'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Student'])),
            ('date_finished', self.gf('django.db.models.fields.DateField')()),
            ('exams_grade', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'myexams', ['ExamsTaken'])

        # Adding model 'Selection'
        db.create_table(u'myexams_selection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Exam'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Question'])),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myexams.Answer'])),
        ))
        db.send_create_signal(u'myexams', ['Selection'])


    def backwards(self, orm):
        
        # Deleting model 'Student'
        db.delete_table(u'myexams_student')

        # Deleting model 'Teacher'
        db.delete_table(u'myexams_teacher')

        # Deleting model 'School'
        db.delete_table(u'myexams_school')

        # Deleting model 'Semester'
        db.delete_table(u'myexams_semester')

        # Deleting model 'Course'
        db.delete_table(u'myexams_course')

        # Deleting model 'StudentCourses'
        db.delete_table(u'myexams_studentcourses')

        # Deleting model 'Exam'
        db.delete_table(u'myexams_exam')

        # Deleting model 'Question'
        db.delete_table(u'myexams_question')

        # Deleting model 'Answer'
        db.delete_table(u'myexams_answer')

        # Deleting model 'ExamsTaken'
        db.delete_table(u'myexams_examstaken')

        # Deleting model 'Selection'
        db.delete_table(u'myexams_selection')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 8, 14, 38, 0, 932713, tzinfo=<UTC>)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 8, 14, 38, 0, 932294, tzinfo=<UTC>)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'myexams.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Question']"})
        },
        u'myexams.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.School']"}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Semester']"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Teacher']"})
        },
        u'myexams.exam': {
            'Meta': {'object_name': 'Exam'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Course']"}),
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'exam_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'return_date': ('django.db.models.fields.DateField', [], {})
        },
        u'myexams.examstaken': {
            'Meta': {'ordering': "['-exam', 'student']", 'object_name': 'ExamsTaken'},
            'date_finished': ('django.db.models.fields.DateField', [], {}),
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Exam']"}),
            'exams_grade': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Student']"})
        },
        u'myexams.question': {
            'Meta': {'object_name': 'Question'},
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Exam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'myexams.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'myexams.selection': {
            'Meta': {'object_name': 'Selection'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Answer']"}),
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Exam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Question']"})
        },
        u'myexams.semester': {
            'Meta': {'object_name': 'Semester'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'year': ('django.db.models.fields.DateField', [], {})
        },
        u'myexams.student': {
            'Meta': {'object_name': 'Student'},
            'enrolled': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'myexams.studentcourses': {
            'Meta': {'object_name': 'StudentCourses'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myexams.Student']"})
        },
        u'myexams.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'hired': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['myexams']
