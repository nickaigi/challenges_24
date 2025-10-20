class Codec:
    def __init__(self) -> None:
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl) -> str:
        """
        This is a very naive approach
        """
        shortUrl = f'http://tinyurl.com/{self.counter}'
        self.url_map[shortUrl] = longUrl
        self.counter += 1
        return shortUrl

    def decode(self, shortUrl) -> str:
        return self.url_map.get(shortUrl, "")
