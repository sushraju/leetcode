import time
import string
import hashlib

class Shortener:
    def __init__(self):
        self.url_map = {}

    def generate_id(self):
        return int(time.time()) * 1000
    
    def encode(self, long_url, base=62):
        id = self.generate_id()
        map = string.digits + string.ascii_letters
        url_hash = hashlib.md5(long_url.encode()).hexdigest()
        url_hash_len = len(url_hash)
        xor_url_hash = int(url_hash[:url_hash_len//3], 16) ^ int(url_hash[url_hash_len//3:-url_hash_len//3], 16) ^ int(url_hash[-url_hash_len//3:], 16)
        short_url = ""

        while xor_url_hash > 0:
            p = xor_url_hash % base
            short_url += map[p]
            xor_url_hash = xor_url_hash // base
        self.url_map[short_url] = long_url
        print(short_url)
        return short_url

    def decode(self, short_url):
        if short_url in self.url_map:
            return self.url_map[short_url]
        return None
    
def main():
    url_shortener = Shortener()
    print(url_shortener.decode(url_shortener.encode("https://coolmonk.org/work1")))
              
if __name__ == "__main__":
    main()