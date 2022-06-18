# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from deutschland.tagesschau.api.api2_api import Api2Api
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.tagesschau.api.api2_api import Api2Api
from deutschland.tagesschau.api.channels_api import ChannelsApi
from deutschland.tagesschau.api.homepage_api import HomepageApi
from deutschland.tagesschau.api.multimedia_api import MultimediaApi
from deutschland.tagesschau.api.news_api import NewsApi
from deutschland.tagesschau.api.newsfeed_api import NewsfeedApi
from deutschland.tagesschau.api.ressort_api import RessortApi
from deutschland.tagesschau.api.search_api import SearchApi
