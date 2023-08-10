# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**96** channels, **371,578.9** hours playtime between **2023-01-17** and **2023-08-11**


### playtime per genre (top 30)

    24628.5h 6.63% Nachrichten
    17633.4h 4.75% Verkaufsshow
    15028.9h 4.04% Krimiserie
    12510.2h 3.37% Werbesendung
    12228.7h 3.29% Dokureihe
    11240.1h 3.02% Dokusoap
    10680.5h 2.87% Regionalmagazin
    9355.9h  2.52% Dokumentation
    9028.2h  2.43% *unknown*
    7028.2h  1.89% Zeichentrickserie
    6792.0h  1.83% Infomercial
    6570.9h  1.77% Animationsserie
    6104.4h  1.64% Comedyserie
    5229.9h  1.41% Morgenmagazin
    4935.0h  1.33% Religionsmagazin
    4889.3h  1.32% Talkshow
    4495.3h  1.21% Magazin
    4174.1h  1.12% Programmende
    3679.8h  0.99% E-Sport
    3499.0h  0.94% Wetterbericht
    3495.2h  0.94% Sitcom
    3377.8h  0.91% Börsenmagazin
    2987.3h  0.80% Quiz
    2922.1h  0.79% Musikmagazin
    2855.6h  0.77% Wirtschaftsmagazin
    2837.4h  0.76% Komödie
    2802.9h  0.75% Wissensmagazin
    2583.9h  0.70% Telenovela
    2413.1h  0.65% Sportmagazin
    2396.9h  0.65% Reportagereihe
