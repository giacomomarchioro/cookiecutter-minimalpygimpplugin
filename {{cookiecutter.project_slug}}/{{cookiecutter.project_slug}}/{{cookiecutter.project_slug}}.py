#!/usr/bin/python
'''
{{cookiecutter.project_short_description}}
'''
from gimpfu import *
 
def {{ cookiecutter.project_name }}(timg, tdrawable):
    print "Hello, world!"
 
register(
        "{{ cookiecutter.project_name }}",
        "{{ cookiecutter.project_short_description }}",
        "{{ cookiecutter.project_short_description }}",
        "{{ cookiecutter.full_name }}",
        "{{ cookiecutter.full_name }}",
        "2010",
        "<Image>/Image/Resize to max...",
        "{{ cookiecutter.image_types }}",
        [],
        [],
        {{ cookiecutter.project_name }})
 
main()
