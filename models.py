# -*- coding: utf-8 -*-

db.define_table('libdb',
                   Field('title', label="Title"),
                   Field('subject',label="Subject"),
                   Field('description', 'text', label="Description"),
                   Field('url', label="Url"), plural="Databases")



db.define_table('stored_item',
                Field('title', label="Title"),
                   Field('subject',label="Subject"),
                   Field('description', 'text', label="Description"),
                   Field('url', label="Url"), plural="Databases")


db.stored_item._enable_record_versioning(archive_db=db,
                                         archive_name='stored_item_archive',
                                         current_record='current_record',
                                         is_active='is_active')
