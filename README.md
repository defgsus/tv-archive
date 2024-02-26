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

**99** channels, **727,044.5** hours playtime between **2023-01-17** and **2024-02-27**


### playtime per genre (top 30)

    47325.2h 6.51% Nachrichten
    34895.8h 4.80% Verkaufsshow
    29510.1h 4.06% Krimiserie
    25110.8h 3.45% Werbesendung
    23280.3h 3.20% Dokureihe
    21960.3h 3.02% Dokusoap
    21060.9h 2.90% Regionalmagazin
    18762.3h 2.58% Dokumentation
    18543.3h 2.55% *unknown*
    13472.0h 1.85% Zeichentrickserie
    13216.6h 1.82% Infomercial
    12795.6h 1.76% Animationsserie
    11013.0h 1.51% Comedyserie
    10296.8h 1.42% Morgenmagazin
    9826.4h  1.35% Religionsmagazin
    9754.8h  1.34% Magazin
    9649.2h  1.33% Talkshow
    7186.8h  0.99% E-Sport
    6917.2h  0.95% Programmende
    6875.7h  0.95% Sitcom
    6481.4h  0.89% Börsenmagazin
    6464.4h  0.89% Wetterbericht
    6165.2h  0.85% Komödie
    6108.0h  0.84% Quiz
    5446.8h  0.75% Wissensmagazin
    5304.5h  0.73% Realityshow
    5270.0h  0.72% Wirtschaftsmagazin
    5224.7h  0.72% Politikmagazin
    5175.9h  0.71% Telenovela
    5006.8h  0.69% Musikmagazin
