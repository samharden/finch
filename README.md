# FINCH KM

## KM for specialized bar associations

## AWS:
sudo ssh -i "finch-kp.pem" ec2-user@ec2-18-206-61-184.compute-1.amazonaws.com
- Note: key pair isn't in github...

## Docker:
sudo docker build -t samharden/finch .
sudo docker run -d -p 80:8000 samharden/finch:latest

## heroku:
git push heroku master

## To-Do (in order of importance):
* Dockerized container of finch on AWS for VTNALEA - serve at vtnalea.finch-km.com  


* Email endpoint with mailgun - example:
* 1.  send email to vtnaela@finch-km.com
* 2.  mailgun does its thing by making a get request on certain parameters
* 3.  Finch parses email to extract:
      Who sent it
      What they're looking for
      What category it falls under
* 4.  Starts discussion thread for that user, and emails the other users
      subscribed to that category with that request.
* 5.  Searches the database for the top 3-4 relevant answers / documents
      and emails the sender with that info and links to those
* 6.  Notifies the sender when someone responds to the thread.

* REFACTORING!
* Re-direct to new question page once question is asked.
* Add users with form template
* Edit user page
* Better log in page
* Email update function
* Drag and drop uploads
* Add elastisearch(?) for front-end searching and full-text search of uploaded docs
* NLP to correlate questions/commments and knowledgebase items
* Clio integration?
* migrate to postgres db?
* Comments on main section pages?
* Pytesseract to analyze uploads
* Email endpoint - you can email its address, and it will throw the content into a question?

* Make profile pages public, Quorum private. Profile pages show docs uploaded by each attorney, practice area, jurisdiction, and ________?
* add to User model: website, practice areas (%), twitter, lexblog account?
* New document model? Allow linking to it internally? make primary?

* Auto-convert image uploads to pdf? - Allows taking photo of doc with phone and uploading...
