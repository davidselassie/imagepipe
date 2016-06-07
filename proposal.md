# Proposal: Image Pipe

**Image Pipe** is a web app that allows artists to upload single **source** images.

Pairs of new images from different artists will be combined together at half opacity each, to produce **mashup** images.
Once an image has been mashed-up, it won't be paired again.

The main page of the site will show a feed of mashed-up images with their pair of artists.

## Specific Functionality

### Main / Gallery Page

The main / gallery page will show a vertical list of mashups.
The ten most recent mashups will be displayed on the page.

In the header, there will be a link to the upload page.

### Upload Page

The upload page will have a form where the user can upload an image.

There will be a confirmation alert if the image is uploaded successfully.

## Data Model

### Source

Each Source is one un-modified image uploaded by a user.

* Unique ID
* Image JPEG data
* Upload timestamp
* Been mashed-up? flag

Sources will need to be looked up by most recent upload timestamp and mashed-up flag.

### Mashup

Each Mashup is a combination of two Images and are the products of the web app.

* Unique ID
* Image JPEG data
* Creation timestamp
* Source Image ID 1
* Source Image ID 2

Mashups will need to be looked up by ID and most recent creation timestamp.

## Technical Components

The Mashup generation module will be a Python module that uses the [Pillow](http://pillow.readthedocs.io/en/3.2.x/) library to combine two images at half opacity.

Source and Mashup data models will be stored and searched using Django Models in a PostgreSQL database.

Mashup image data will be exposed as JPEG files via a ID-lookup endpoint, but piped directly out of the DB from a Django model lookup.

Front-end HTML will be generated using Django templates with fixed CSS layout and style.
jQuery will be used to provide interactive feedback on upload of images.
Mashups for the gallery will be found via a Django model query against the existing Mashups.

Source upload will be handled via multi-part POST, only JPEG upload will be supported, and funneled directly into the DB via Django models, including image data.

Component Source selection code will pick the least-recently uploaded un-paired Source for mashing-up.

A background mashup queueing component will be kicked off when a new Source is uploaded and will run the component Image selection code, the Mashup generation code, and the mashup saving code in that order.
It will not delay the acknowledgement of successful Source uploading.

## Schedule

* Mashup generation module - easy - 1 day
* Source and Mashup DB storage - medium - 2 days
* Mashup file endpoint - easy - 1 day
* Existing Mashup gallery selection - easy - 0.5 day
* Basic viewing of existing Mashups - medium - 4 days
* Source upload and storage pipeline - medium - 3 days
* Component Source selection code - easy - 0.5 day
* Background mashup queueing - hard - 5 days

## Further Work

* A JSON endpoint to return relevant Mashup objects.
* Infinite scrolling of the main page using that endpoint.
* Add a Artist table and require login to upload.
* Add an artist page which shows all mashups containing a source image by that artist.
* Intelligent selection of image pairs using disjoint image density.
