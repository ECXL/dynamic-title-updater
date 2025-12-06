# dynamic-title-updater
This code utilises Selenium and the [Worldometers website](https://www.worldometers.info/world-population/) to provide a live number of the world population to update a YouTube title dynamically.

There is also a version using [REST Countries API](https://restcountries.com/?ref=public_apis) found in `main-api.py`. This version was created in case the website used in main updates its format in a way that messes up the code. Not as accurate as the Worldometers but should be less likely to break in the future.

*Inspired by Tom Scott's view count updating YouTube video.*

Made this to update an old video idea about a dynamic YouTube title revolving around the current world population. Code broke a while back so writing new code for it from the ground up.

## Requirements

```
pip install -r requirements.txt
```
YouTube account and a YouTube data API project on Google Cloud with credentials to edit YouTube title. Guide on how to do that is on YouTube's [Obtaining authorization credentials guide](https://developers.google.com/youtube/registering_an_application) and on Google's [Using OAuth 2.0 to Access Google APIs guide](https://developers.google.com/identity/protocols/oauth2). Generate client secret and put it into a file called `CLIENT_SECRET.json`. Example for how it should look in `example_CLIENT_SECRET.json`.

Uploaded YouTube video. Get the YouTube video id (not the same as the full url) and put it into a `.env` in the same format as `example.env` (wihout the square brackets).