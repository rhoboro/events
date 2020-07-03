from dataclasses import dataclass, asdict, fields
import time

import requests
from bs4 import BeautifulSoup

from .constants import SESSIONS_URL


@dataclass(frozen=True)
class Session:
    title: str
    speaker: str
    video: str
    content: str
    url: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def create(cls, url, detail_soup):
        # 動画リンクはない場合もある
        if (watch_on_youtube := detail_soup.find(text="Watch on YouTube")) :
            video = watch_on_youtube.previous_element["href"]
        else:
            video = ""

        return Session(
            title=detail_soup.find("h2").text,
            speaker=detail_soup.find(text="Presented by:").next_element.next_element.text,
            video=video,
            content=detail_soup.find(class_="description").text,
            url=url,
        )

SESSION_FIELDS = [field.name for field in fields(Session)]


def _get_sessions():
    sessions = requests.get(SESSIONS_URL)
    soup = BeautifulSoup(sessions.text, "html.parser")
    talks = soup.find(id="talks").next_element.next_element.next_element.find_all("li")
    for talk in talks:
        detail_url = talk.find_all("a")[1]["href"]
        detail = requests.get(detail_url)
        detail_soup = BeautifulSoup(detail.text, "html.parser")
        yield Session.create(detail_url, detail_soup)
        time.sleep(1)


def scrape():
    yield from _get_sessions()
