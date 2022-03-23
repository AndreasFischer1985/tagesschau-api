# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.tagesschau.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.tagesschau.model.channels_response import ChannelsResponse
from deutschland.tagesschau.model.channels_response_channels import (
    ChannelsResponseChannels,
)
from deutschland.tagesschau.model.homepage_response import HomepageResponse
from deutschland.tagesschau.model.homepage_response_news import HomepageResponseNews
from deutschland.tagesschau.model.homepage_response_regional import (
    HomepageResponseRegional,
)
from deutschland.tagesschau.model.multimedia_response import MultimediaResponse
from deutschland.tagesschau.model.news_response import NewsResponse
from deutschland.tagesschau.model.news_response_news import NewsResponseNews
from deutschland.tagesschau.model.search_response import SearchResponse
from deutschland.tagesschau.model.search_response_search_results import (
    SearchResponseSearchResults,
)
