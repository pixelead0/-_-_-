import requests
from bs4 import BeautifulSoup
import urllib3
from typing import Dict, AnyStr


import logging

logger = logging.getLogger(__name__)
urllib3.disable_warnings()


class JudgmentHelper(object):
    """Helper for judgment."""

    def extract_info(self, url_poder_judicial: str) -> Dict[str, AnyStr]:
        """Extract judgment info from poderjudicialvirtual.com"""
        s = requests.Session()
        res = s.get(url_poder_judicial, verify=False)

        soup = BeautifulSoup(res.text)
        t = soup.select("div#pcont div.content p")[0].text.split()
        c = soup.select("div#pcont div.content p")[1].text.split()

        text = " ".join(t)

        court_pos = text.find(" > ")
        actor_pos = text.find("Actor:")
        defendant_pos = text.find("Demandado:")

        actor = text[actor_pos + 7 : defendant_pos - 1]
        defendant = text[defendant_pos + 11 :]
        court = text[court_pos + 3 : actor_pos - 1]
        state = text[:court_pos]

        case_file = c[3]
        notifications = c[-2]
        c.pop(0)
        resume = " ".join(c)

        data = {
            "url": url_poder_judicial,
            "actor": actor,
            "defendant": defendant,
            "court": court,
            "state": state,
            "case_file": case_file,
            "notifications": notifications,
            "resume": resume,
        }

        return data
