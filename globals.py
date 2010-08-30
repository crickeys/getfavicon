import logging

inf = logging.info
war = logging.warning
err = logging.error
cri = logging.critical

SHARDS_PER_COUNTER = 1000
MC_CACHE_TIME = 2419200 #seconds (28 days)
DS_CACHE_TIME = 90 #days

# Surpresses the index and test pages
HEADLESS = False

COUNTERS = [
  "favIconsServed",
  "favIconsServedDefault",
  "cacheNone",
  "cacheMC",
  "cacheDS",
]