# -*- coding: utf-8 -*-

import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

salt = 'will'

def calc_md5(password):
    if password in db:
        print(db[password])
    else:
        print('not exist')

def login(user, pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    pwd = md5.hexdigest()
    if (user in db) and (db[user] == pwd):
        print('true')
        return True
    else:
        print('false')
        return False

def register(uname, upwd):
    db[uname] = get_md5(upwd + uname + 'will')

calc_md5('bob')
login('michael', '123456')