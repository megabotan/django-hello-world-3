MANAGE=python django_hello_world/manage.py
PYTHONPATH=`pwd`

test:
	DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) test hello

check_syntax:
	flake8 --exclude=migrations django_hello_world/hello

run:
	DJANGO_SETTINGS_MODULE=django_hello_world.settings $(MANAGE) runserver

syncdb:
	DJANGO_SETTINGS_MODULE=django_hello_world.settings 
	$(MANAGE) syncdb --noinput  
	$(MANAGE) migrate
