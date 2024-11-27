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

**109** channels, **1,158,122.3** hours playtime between **2023-01-17** and **2024-11-28**


### playtime per genre (top 30)

    75613.6h 6.53% Nachrichten
    52872.8h 4.57% Verkaufsshow
    48327.3h 4.17% Krimiserie
    42651.1h 3.68% Werbesendung
    36114.8h 3.12% Dokureihe
    34475.9h 2.98% Dokusoap
    33908.3h 2.93% Regionalmagazin
    30458.7h 2.63% Dokumentation
    27277.2h 2.36% *unknown*
    21697.4h 1.87% Zeichentrickserie
    21391.2h 1.85% Infomercial
    20698.4h 1.79% Animationsserie
    16545.8h 1.43% Comedyserie
    16215.6h 1.40% Morgenmagazin
    15411.1h 1.33% Religionsmagazin
    15359.1h 1.33% Talkshow
    14418.5h 1.24% Magazin
    11440.1h 0.99% E-Sport
    11186.0h 0.97% Sitcom
    10460.9h 0.90% Wetterbericht
    10244.1h 0.88% Quiz
    10231.8h 0.88% Programmende
    10148.0h 0.88% Komödie
    8902.5h  0.77% Realityshow
    8813.3h  0.76% Politikmagazin
    8702.8h  0.75% Wissensmagazin
    8604.5h  0.74% Börsenmagazin
    7751.9h  0.67% Wirtschaftsmagazin
    7669.2h  0.66% Telenovela
    7651.9h  0.66% Dramaserie
