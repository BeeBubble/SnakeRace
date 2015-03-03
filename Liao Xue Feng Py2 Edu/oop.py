# -*- coding: utf-8 -*
__author__ = 'shawn'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


shawn = Student('Shawn', 99)
shawn.print_score()
