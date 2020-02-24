from dataclasses import asdict, dataclass, fields

import requests
from bs4 import BeautifulSoup

from .constants import BASE_URL, SESSIONS_URL


@dataclass(frozen=True)
class _Session:
    title: str
    speaker: str
    level: str
    category: str
    url: str
    content: str

    @classmethod
    def create(cls, url, soup):
        session_attr = soup.find_all("span", class_="badge")
        return _Session(
            url=url,
            title=soup.find("h1", class_="session-title").text,
            speaker=soup.find("address", class_="speaker-name").text.strip().replace("By: ", ""),
            level=session_attr[0].text,
            category=session_attr[1].text,
            content="\n".join(
                p.get_text() for p in soup.find("div", class_="session-content").find_all("p")
            ),
        )

    def to_dict(self):
        return asdict(self)


def _get_sessions():
    sessions = requests.get(SESSIONS_URL)
    soup = BeautifulSoup(sessions.text, "html.parser")
    for session in soup.find_all("article", class_="session"):
        detail_url = BASE_URL + session.find("a")["href"]
        detail = requests.get(detail_url)
        detail_soup = BeautifulSoup(detail.text, "html.parser")
        yield _Session.create(detail_url, detail_soup)


def scrape():
    yield from _get_sessions()


SESSION_FIELDS = [field.name for field in fields(_Session)]
