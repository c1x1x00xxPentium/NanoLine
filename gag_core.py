from nineapi.nineapi.client import  Client, APIException
import os
import random

class Sections:
    ANIME_MANGA = 32
    WTF         = 4
    SAVAGE      = 45
    KPOP        = 34
    COMIC       = 17

class Gag:
    def __init__(self):
        self.gag_client = Client()
        self.gag_client.log_in(str( os.environ.get('GAG_USERNAME')), str(os.environ.get('GAG_PASSWORD')))

    def get_post_from(self, group_id):
        post = random.choice( 
            self.gag_client.get_posts(
                group=group_id, count=50, 
                type_='hot', 
                entry_types=['photo']
                )
            )
        return post