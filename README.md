# phish_decode
Decodes repeatedly encoded JS base64 strings for de-obfuscation of HTML phishing attachments. 


Usage: 

$ phish_decode.py [-h] -f FILE [-r ROUNDS]
  
  -h, --help                  show this help message and exit
  -f FILE, --file FILE        Input file
  -r ROUNDS, --rounds ROUNDS  Maximum rounds to try



TODO:
* Add additional string types.
* Improve auto-detection/make phish message agnostic
