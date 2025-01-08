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

**110** channels, **1,220,368.3** hours playtime between **2023-01-17** and **2025-01-09**


### playtime per genre (top 30)

    79799.1h 6.54% Nachrichten
    55199.9h 4.52% Verkaufsshow
    50592.5h 4.15% Krimiserie
    45264.3h 3.71% Werbesendung
    38000.7h 3.11% Dokureihe
    35885.8h 2.94% Dokusoap
    35532.4h 2.91% Regionalmagazin
    32512.0h 2.66% Dokumentation
    29032.9h 2.38% *unknown*
    22953.1h 1.88% Zeichentrickserie
    22590.4h 1.85% Infomercial
    21805.4h 1.79% Animationsserie
    17173.5h 1.41% Comedyserie
    17025.9h 1.40% Morgenmagazin
    16073.5h 1.32% Talkshow
    15967.9h 1.31% Religionsmagazin
    14897.3h 1.22% Magazin
    12074.2h 0.99% E-Sport
    11690.1h 0.96% Sitcom
    11196.2h 0.92% Komödie
    11050.5h 0.91% Wetterbericht
    10811.1h 0.89% Quiz
    10721.1h 0.88% Programmende
    9448.1h  0.77% Realityshow
    9292.9h  0.76% Politikmagazin
    9059.5h  0.74% Wissensmagazin
    8771.4h  0.72% Börsenmagazin
    8079.2h  0.66% Wirtschaftsmagazin
    8075.4h  0.66% Arztserie
    8075.4h  0.66% Dramaserie
