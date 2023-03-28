# SBEO Django Project

Django app by SBEO currently beeing built with following app:
RMS - Referee Management System: Referees can set their availability for each event and the referee commission can select which get an invitation

## Current status

This project is currently being developed and has the goal to be a first functional version in Summer 2023.

All text fields are translatable and even the whole application can be served in multiple languages, though the user entered data cannot be translated. For customising the text you can directly edit the translation files or create translations for additional languages and set them as default in the `settings.py` file. For details see the Django documentation for internationalisation.

## Requirements

The requirements are kept upto-date in the `requirements.txt` file. It is tested to run on Ubuntu-2004 but should work on any unix operating system with python3.

## Installation

In order to install and use the system for your own purposes, you should first clone the repository and adopt the static information as necessary.

The local settings are loaded from environment variables. The following variables are loaded in `settings.py`and should be set to allow proper functionality. Their names should be self-explanatory, otherwise you can see where they are loaded in `settings.py`and search for the respective settings and allowed values.

```
DJANGO_SECRET_KEY
```

Once you have made the necessary adoptions, you are ready for deployment. You can follow for example the instruction on [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04), where instead of creating a new project you can clone your customised repository. When creating the `gunicorn.service` file, in the `[service]` section make sure to include `EnvironmentFile=` followed by the absolute path to a file containing your environment variables in the format `variable='value'` without any export directives. Only then gunicorn will be able to load the environment variables and start the server.

Once everything is working, you should finalise the deployment by switching the debug flag in `setting.py` to false and entering the allowed hostname in the same field. Make sure everything turns up when restarting the machine. As a last word of caution keep in mind that this is potentially a public-facing server which should be secured accordingly, including regular security upgrades, limiting ssh-access, proper firewall configuration and SSL-certificates for transmitting passwords upon registration.

## First Use

After setting up a new instance of this service you should log in with the superuser created from the command-line and supply as much additional information as you like. The following groups are created automatically.

# Contribution

As we do not intend to make any financial profit of this Application, we decided to make this tool available for everyone. I know that there are probably dozens of ways to improve the tool and am steadily working on improving existing functionality and adding new function. If you notice any bugs or want to add any new features, make it easier for others to adopt, feel free to create an issue or a pull request.

If you want to support the project in any other way, feel free to contact me directly.
