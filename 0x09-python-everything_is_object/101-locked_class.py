#!/usr/bin/python3
class LockedClass:
    """A locked class that prevents the user from
    dynamically creating new instance attributes"""
    __slots__ = ['first_name']
