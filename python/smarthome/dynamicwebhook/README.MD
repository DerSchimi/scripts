Simple python dynamic webhook.
When using ifttt or something similar to invoke a webhook, you can use this python 
script. Start the script and all POST Requests will be redirected to the shellscript.
Alter the shellscript to your needs. No need to alter or restart the python script.

ifttt settings:
 path: /dynwebhook
 method: Post
 contentType:  text/plain
 body: parameter value 


To start the script on boot, add a cronjob like this:

@reboot cd <dynwebhookdir> && /usr/bin/python3 dynwebhookserver.py >> webhook.log&

