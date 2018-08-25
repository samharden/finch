# FINCH KM

## KM for specialized bar associations
### Just use docker:

sudo docker run -d -p 80:8000 samharden/finch:latest

## heroku:
If you want to run it on heroku it's also got a procfile

## Administraton UN and PW:
- admin
- MyPassword

Go to admin panel at localhost/admin

## File Uploads:
You'll need an Amazon AWS S3 bucket.
Put in your credentials in the crm/settings.py file where indicated.

## Email notifications:
If you have a domain, use mailgun.
Put in your API key and details in the settings.py file.


Yay!
