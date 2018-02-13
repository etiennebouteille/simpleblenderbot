#!/usr/bin/env python
import sys
from twython import Twython



# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = 'P9dy0nSFl8iGc7qq4dvybiiWl'
apiSecret = 'jBv4wCaFiQEMRFQp4qsQnfU32HKSNu177NWbd7DfZJTPbYJAiC'
accessToken = '894260522073432064-7IgPyrYVapJ9PIusuRLnm4iw2f7hAz3'
accessTokenSecret = 'FBtTNk60GErIkJy3UcL8L3rWijEUdRslcuLMXplnbMmFc'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

photo = open('/home/pi/robot/mypicture.png')
response = api.upload_media(media=photo)
api.update_status(status=tweetStr, media_ids=[response['media_id']])

