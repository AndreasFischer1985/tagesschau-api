[[DE]](README.md)/[[EN]](README_en.md)

# Tagesschau API

The Tagesschau is a news program of the ARD (abbreviation for "Arbeitsgemeinschaft der öffentlich-rechtlichen Rundfunkanstalten der Bundesrepublik Deutschland"), which is produced by ARD-aktuell in Hamburg and broadcast several times a day. ARD-aktuell has been the central television news department of ARD since 1977, which in turn is a broadcasting association consisting of the state broadcasting corporations and Deutsche Welle.

Current news and media articles are available in JSON format on [www.tagesschau.de](https://www.tagesschau.de) via the API documented here.


## API2

**URL:** https://www.tagesschau.de/api2/

Important news and breaking news, as well as regional news from path '/homepage/'. 

API2 succeeds the previous API, which according to its own statement has been obsolete since October 1st, 2018 (cf. https://www.tagesschau.de/api/ - although there are still up to date post to be found there, e.g., under https://www.tagesschau.de/api/ inland/, https://www.tagesschau.de/api/ausland/, https://www.tagesschau.de/api/wirtschaft/ and https://www.tagesschau.de/api/regional/).


## Homepage

**URL:** https://www.tagesschau.de/api2/homepage/

Selected news and breaking news that are shown on the homepage of the Tagesschau app.


## News

**URL:** https://www.tagesschau.de/api2/news/

Current news that can be filtered via GET parameters:

**Parameter:** *regions* 
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16

State: 1=Baden-Württemberg, 2=Bavaria, 3=Berlin, 4=Brandenburg, 5=Bremen, 6=Hamburg, 7=Hesse, 8=Mecklenburg-Western Pomerania, 9=Lower Saxony, 10=North Rhine-Westphalia, 11= Rhineland-Palatinate, 12=Saarland, 13=Saxony, 14=Saxony-Anhalt, 15=Schleswig-Holstein, 16=Thuringia. Multiple comma-separated specifications possible (e.g. regions=1,2).


**Parameters:** *ressort*

- inland
- ausland
- wirtschaft
- sport	
- video

Department/subject area


## Newsfeed

**URL:** https://www.tagesschau.de/api2/newsfeed-101~_date-{datumsangabe}.json

News and breaking news on a selected date in the recent past (up to about a month), filtered using the path parameter **datumsangabe** in the format yymmdd (e.g. 220228 for 02/28/2022").


## Search

**URL:** https://www.tagesschau.de/api2/search/


**Parameter:** *searchText* 

search text


**Parameter:** *resultPage* 

page


**Parameter:** *pageSize* 

Search results per page (1-30)


## Department

**URL:** https://www.tagesschau.de/api2/{ressort}/

Department-specific messages, filtered via the path parameter **ressort** (e.g. inland, ausland or wirtschaft)


## Channels

**URL:** https://www.tagesschau.de/api2/channels/

Current channels (im Livestream: tagesschau24, tagesschau in 100 Sekunden, tagesschau, tagesschau 20 Uhr, tagesthemen, nachtmagazin, Bericht aus Berlin, tagesschau vor 20 Jahren, tagesschau mit Gebärdensprache)


## Multimedia

**URL:** https://www.tagesschau.de/api2/multimedia/

Multimedia content.


## Example

```bash
tagesschau=$(curl -m 60 https://www.tagesschau.de/api2/homepage/)
```
