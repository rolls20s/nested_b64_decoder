# phish_decode
Decodes repeatedly encoded JS base64 strings for de-obfuscating HTML phishing attachments.


Usage:

phish_decode.py [-h] -f FILE [-r ROUNDS]  
Flag | Description
------|------
-h, --help        |          show this help message and exit  
-f FILE, --file FILE |       Input file  
-r ROUNDS, --rounds ROUNDS|  Maximum rounds to try  



TODO:
- [ ] Add support for additional encoding types.
- [ ] Improve auto-detection/make message-agnostic
