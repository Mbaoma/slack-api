import requests 

# type in a link to the API method: files.upload 
url = "https://slack.com/api/files.upload" 

# type in the Bot User OAuth Token 
bot_token = {"token":"xoxb-xxxxxx-xxxxxx-xxxxxx"} 

# type in the channel(s) to send files to 
channels = { "channels":["plan-budget"]} 

# type in the details of the file to be sent
files = ["./dummy-file.txt", "./dummy-file2.md"]

# write a for loop that helps assign files to file_to_upload, one at a time.
for file in files:
    file_to_upload = { "file":(file, 
                open(file, "rb"), "auto") 
            } 

# here, we define how our response would be
response = requests.post(url, params=channels,  data=bot_token, files=file_to_upload, )
print(response)