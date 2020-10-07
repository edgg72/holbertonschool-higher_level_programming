#!/usr/bin/python3
"""
class Student
"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            new = {}
            for i in range(len(attrs)):
                if type(attrs[i]) is str:
                    continue
                else:
                    break
            for i in attrs:
                try:
                    new[i] = self.__dict__[i]
                except:
                    pass
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
