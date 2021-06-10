from instapy import InstaPy
from instapy import smart_run
from dotenv import load_dotenv
import os

load_dotenv()

session = InstaPy(username=os.getenv("LAMIA_LOGIN"), 
                  password=os.getenv("LAMIA_SENHA")) #login e senha do usuario

with smart_run(session): 
  
  session.follow_user_followers(['filipedeschamps'], amount=500,
                                randomize=False, interact=False)
  
  session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                        style="FIFO",
                        unfollow_after=12 * 60 * 60, sleep_delay=601)
  
  session.follow_user_followers(['filipedeschamps'], amount=500,
                                randomize=False, interact=False)
    
  session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                          style="FIFO",
                          unfollow_after=12 * 60 * 60, sleep_delay=601)
  
  session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                        style="FIFO", unfollow_after=24 * 60 * 60,
                        sleep_delay=601)
