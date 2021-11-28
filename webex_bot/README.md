## Prerequisites:

- [ ] node.js (minimum supported v8.0.0 & npm 2.14.12 and up)

- [ ] Sign up for Webex Teams (logged in with your web browser)


----

## Steps to get the bot working

1. Create a Webex Teams bot (save the API access token and username): https://developer.webex.com/my-apps/new/bot

2. Sign up for nGrok, then connect and start it on your machine (save the port number and public web address): https://ngrok.com/download

3. After installing ngrok, run it on your local machine to get a public ip address, eg `ngrok http 3000`
 
4. Copy the ip address displayed in the ngrok window, ie: : https://1234.eu.ngrok.io

5. Edit  `config.json` with the following values:

* token - Set this to the token for your bot that you got in step 1
* port - Set this to the port you set when you started ngrok in step 3 (ie: 3000)
* webhookUrl - Set this to the ip address that you copied in step 4

6. Turn on your bot server with ```npm start```

7. Add the bot (by its username) to the spaces you want it to be in Webex Teams
