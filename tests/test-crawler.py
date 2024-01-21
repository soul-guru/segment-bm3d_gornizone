import numpy as np
import requests
from bs4 import BeautifulSoup
from rich import print

from sdk.modules.context_to_3d import context_to_3d
from sdk.modules.scan_closest_points_and_links import scan_closest_points_and_links
from sdk.modules.throws import EmptyContext, InsufficientContext
from sdk.plugins.nbc_news_crawler import get_last_nbc_news

array = []
news = get_last_nbc_news()

t = 0
for headline in news:
    t += 1
    print(f"🧠 Training... [{t}/{len(news)}]")
    array.append(context_to_3d(headline, True, True, True))
   
   
while True:
   phrase = input(">> ")
   
   try:
      axis = context_to_3d(phrase)
   except EmptyContext:
      print("Empty context")
      axis = None
   except InsufficientContext:
      print("Insufficient context")
      axis = None
      
   if axis:
      for query in axis[1]:
         print(
            scan_closest_points_and_links(
               array,
               [
                  np.float32(query[0][0]),
                  np.float32(query[0][1]),
                  np.float32(query[0][2]),
                  query[1],
               ],
               0.000001
            )
         )
   
    