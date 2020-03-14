# Youtube Video Uploader

A script to bypass Youtube Data API's 10.000/day query limit (every video query costs like 1.6k so that's 6 videos per day).

This script will do the following:

- Use a slightly changed version of the library in the link here: https://github.com/n8henrie/pycookiecheat,
to get YouTube cookies from user's default Chrome browser.

- Operate with Selenium Webdriver to automate the video uploading procedure to YouTube.

# How To

1. Create a json file which would hold all the parameters of a YouTube video.

2. Create an Uploader object.

```
  from uploader import Uploader

  file_path = /path/to/{filename}.json

  uploader = Uploader()
  
```

3. Initiate the upload via passing the json file path to upload_video function
```
  uploader.upload_video(file_path)
```
