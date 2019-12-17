import re


class Page:

    def __init__(self, status=None,
                 body=None, content_length=0,
                 headers=None, content_type=None,
                 charset=None, title=""):
        self.status = status
        self.body = body
        self.content_length = content_length
        self.headers = headers
        self.content_type = content_type
        self.charset = "utf-8" if charset is None else charset
        self.title = title
        self.get_title()

    def get_title(self):
        if self.body is None:
            return
        if isinstance(self.body, bytes):
            body = self.body.decode(self.charset, errors="ignore")
        title = re.findall("<title>([\s\S]*?)</title>", body)
        if len(title):
            self.title = title[0]
        return self.title

    @staticmethod
    def get_title_from_body(body=None, charset="utf-8"):
        if body is None:
            return
        if isinstance(body, bytes):
            body = body.decode(charset, errors="ignore")
        title = re.findall("<title>([\s\S]*?)</title>", body)
        if len(title):
            title = title[0]
            return title
        return ""
