{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

Features
--------

* TODO

Installing the plug-in
--------

The instruction for installing the plug-in can be found at the following site:

<https://en.wikibooks.org/wiki/GIMP/Installing_Plugins>

Credits
-------

This package was created with Cookiecutter_ and the `giacomomarchioro/cookiecutter-minimalpygimpplugin`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`giacomomarchioro/cookiecutter-minimalpygimpplugin`: https://github.com/audreyr/cookiecutter-pypackage
