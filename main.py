import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from time import sleep

import requests

import os
YOUTUBE_ID = os.getenv("YOUTUBE_ID")

# read/write auth access
auth_level = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def fetch_total_population():
    # fetch number of people from REST countries API
    url = "https://restcountries.com/v3.1/all?fields=population"

    try:
        

        return total_population

    except Exception as e:
        print(f"Error updating title: {e}")

    # if the request get does not work, it returns None
    return None


def main():
    # initialise
    api = "youtube"
    api_version = "v3"
    client_secrets_file = "CLIENT_SECRET.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, auth_level)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api, api_version, credentials=credentials)
    
    while (True):
        try:
            # request YouTube video of choice (youtube-video-id)
            request = youtube.videos().list(
                part="snippet,statistics",
                id=YOUTUBE_ID
            )
            response = request.execute()

            # extract video information
            data = response["items"][0] # 0 needed here even though only one video should return from response
            vid_snippet = data["snippet"]
            title = vid_snippet["title"]
            
            # for user to check and debug in console
            print("Title of Video: " + title)

            total_population = fetch_total_population()

            if total_population is None:
                raise ValueError("Failed to calculate total population")

            print(f"Total population: {total_population:,}")

            # update title
            title_updated = f"THERE ARE {total_population:,} PEOPLE ON EARTH"

            if title != title_updated:
                vid_snippet["title"] = title_updated
                request = youtube.videos().update(
                    part="snippet",
                    body={
                        "id": YOUTUBE_ID,
                        "snippet": vid_snippet
                    }
                )
                response = request.execute()
                print("Updated to: " + title_updated)
            else:
                print("Title already most recent API call")


        except Exception as e:
            print(f"Error updating title: {e}")

        sleep(60*10) # update every ten minutes


if __name__ == "__main__":
    main()