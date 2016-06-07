# ImagePipe

**ImagePipe** is a web app that allows artists to upload single **source** images which will be paired together to produce **mashup** images.

Check out the [full proposal](proposal.md).

## Setup

A `media` directory needs to be made in repository root to hold uploaded images.

The web app can be started by running `python manage.py runserver` in a virtualenv with the included dependencies.

## Usage

You can upload images via the "Upload" link at the top of the page,.
Once you've uploaded two images, they will be mashed-up in the background and will appear on the main page.
