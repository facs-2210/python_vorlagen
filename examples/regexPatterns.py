import re

example1 = '\
XgwDBH8AAAEAAHE2NZsAAAAJ 212.254.91.26 - - [01/01/2020:03:25:08 +0100] "GET /user/ HTTP/1.1" 302 232 \
XgwDBH8AAAEAAHE2NZwAAAAJ 212.254.91.26 - - [01/01/2020:03:25:08 +0100] "GET /user/?__cookie_try=1 HTTP/1.1" 302 217 \
XgwDBH8AAAEAAHE2NZ0AAAAJ 212.254.91.26 - - [01/01/2020:03:25:08 +0100] "GET /user/ HTTP/1.1" 302 - \
XgwDBX8AAAEAAHE2NZ4AAAAJ 212.254.91.26 - - [01/01/2020:03:25:09 +0100] "GET /user/login/ HTTP/1.1" 200 3112'

regexAccessLog = r'(?P<request_id>.*?) (?P<ip>.*?) (.+?) (?P<datetime>\[.*?\]) \"(?P<method>.*?) (?P<url>.*?) (?P<version>HTTP\/.+?)\" (?P<status>[0-9]{3}) (?P<size>[0-9]+|-)'
print(re.match(regexAccessLog, example1).groups())



example2 = '\
45.153.227.31 - adva [24/Dec/2020:13:46:36 +0100] "GET /index.php?option=com_contact&view=contact&id=1 HTTP/1.1" 200 9873 "-" "Mozilla/5.0(Linux;Android10;SAMSUNGSM-A202F)AppleWebKit/537.36(KHTML,likeGecko)SamsungBrowser/12.1Chrome/79.0.3945.136MobileSafari/537.36" "-" \
45.153.227.31 - - [24/Dec/2020:13:46:37 +0100] "POST /index.php?option=com_contact&view=contact&id=1 HTTP/1.1" 200 188 "-" "Mozilla/5.0(Linux;Android10;SAMSUNGSM-A202F)AppleWebKit/537.36(KHTML,likeGecko)SamsungBrowser/12.1Chrome/79.0.3945.136MobileSafari/537.36" "-" \
62.138.3.52 - - [24/Dec/2020:13:47:56 +0100] "GET /robots.txt HTTP/1.1" 200 304 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0" "-" \
62.138.3.52 - - [24/Dec/2020:13:47:56 +0100] "GET / HTTP/1.1" 200 10479 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0" "-" \
185.85.190.132 - - [24/Dec/2020:13:48:23 +0100] "GET / HTTP/1.1" 200 10439 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" "-"'

common_log_regex = r'(?P<ip>.+?) (?P<identifier>.+?) (?P<user>.+?) \[(?P<datetime>.+?)\] "(?P<method>[A-Z]+?) (?P<url>.+?) (?P<version>HTTP\/.+?)\" (?P<status>[0-9]{3}) (?P<size>[0-9]+|-)'
print(re.match(common_log_regex, example2).groups())
