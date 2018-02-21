#!/usr/bin/python
'''
{{cookiecutter.project_short_description}}
'''
from gimpfu import *
 
def {{ cookiecutter.project_slug }}(img,drw):
    img=gimp.image_list()[0]
    layers = img.layers
 
register(
        "{{ cookiecutter.project_slug }}",
        "{{ cookiecutter.project_short_description }}",
        "{{ cookiecutter.project_short_description }}",
        "{{ cookiecutter.full_name }}",
        "{{ cookiecutter.full_name }}",
        "2010",
        "<Image>/Plugins/{{ cookiecutter.project_slug }}",
        "{{ cookiecutter.image_types }}",
        [],
        [],
        {{ cookiecutter.project_slug }})
main()
