# -*- coding: utf-8 -*-

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField


def next_id():
    return '%015d%s000' % (int(time.time()) * 1000, uuid.uuid4().hex)


class User(Model):
    __table__='users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time())


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    sub_name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time())


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time())


class ACFcous(Model):
    __table__ = 'acfun_focus'

    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_id = IntegerField()
    user_img = StringField(ddl='varchar(255)')
    avatar = StringField(ddl='varchar(255)')
    sign = StringField(ddl='varchar(255)')
    title = StringField(ddl='varchar(50)')
    title_img = StringField(ddl='varchar(255)')
    url = StringField(ddl='varchar(50)')
    release_date = StringField(ddl='varchar(50)')
    description = StringField(ddl='varchar(50)')
    tags = StringField(ddl='varchar(255)')
    video_time = IntegerField()


class JinGuang(Model):
    __table__ = 'jinguang'

    id = IntegerField(primary_key=True)
    pid = IntegerField()
    title = StringField(ddl='varchar(50)')
    title_url = StringField(ddl='varchar(50)')
    post_time = StringField(ddl='varchar(50)')
    add_time = FloatField(default=time.time())