# -*- coding: utf-8 -*-

class Student(object):

    #__slots__ = ('name', 'score')

    def __init__(self, name, score, birth, age = 0):
        self.__name = name
        self.__score = score
        self.__birth = birth
        self.__age = age

    def __str__(self):
        return 'Student object (name=%s)' % self.__name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'grade':
            return '高一'
        raise AttributeError('\'Student\' object hash no attribute \'%s\' ' % attr)

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            print('A')
        elif self.__score >=60:
            print('B')
        else:
            print('C')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 1:
            self.__name = name
        else:
            raise ValueError('bad name')

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):

        if not isinstance(score, int):
            raise ValueError('score must be an integer')

        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('score must between 1 ~ 100')

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2017 - self.__age


will = Student('will', 55, '1991-12-02')
sarcasme = Student('sarcasme', 60, '1991-01-06')
will.print_score()
sarcasme.print_score()

#bart = Student()
#bart.set_name('Bast Simpson')
#print(bart.get_name())

will.get_grade()

will.score = 60
print(will.score)
#will.score = 999

print(will)
#bart.set_score(999)
print(will.grade)
print(will.some)

