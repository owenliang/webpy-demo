# -*- coding: utf-8 -*-

from . import db_webpy

# 模型层
#create table user(id int not null auto_increment primary key,name varchar(10));
class user_model:
    def insert_user(name):
        row = {'name': name}
        return db_webpy.insert('user', **row)