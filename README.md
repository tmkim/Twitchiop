Twitchdiol (Because Twitchio was already taken...)

APIs/Libraries:
Twilio API
Twitch.tv API
boto (Amazon S3)
urllib2
requests
ffmpeg (will make a console call on ubuntu)

How to use:

1. Run vid2aud.py
  2. Enter your phone number
  3. Enter the name of a Twitch.tv channel
  4. Twitchdiol will pick a random previous broadcast from this channel
  5. Twitchdiol will then download this broadcast, use ffmpeg to extract the audio, then upload it to Amazon S3
  6. Twitchdiol will then call you and play back this audio file.
