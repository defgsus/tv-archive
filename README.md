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

**99** channels, **659,525.0** hours playtime between **2023-01-17** and **2024-01-20**


### playtime per genre (top 30)

    43063.2h 6.53% Nachrichten
    31528.0h 4.78% Verkaufsshow
    26510.9h 4.02% Krimiserie
    22497.3h 3.41% Werbesendung
    21418.5h 3.25% Dokureihe
    19732.2h 2.99% Dokusoap
    19018.7h 2.88% Regionalmagazin
    17089.0h 2.59% Dokumentation
    16449.8h 2.49% *unknown*
    12193.4h 1.85% Zeichentrickserie
    11973.2h 1.82% Infomercial
    11590.4h 1.76% Animationsserie
    9993.1h  1.52% Comedyserie
    9349.4h  1.42% Morgenmagazin
    8910.8h  1.35% Religionsmagazin
    8737.9h  1.32% Magazin
    8715.1h  1.32% Talkshow
    6485.9h  0.98% E-Sport
    6384.4h  0.97% Programmende
    6357.8h  0.96% Sitcom
    5954.9h  0.90% Wetterbericht
    5869.8h  0.89% Börsenmagazin
    5590.4h  0.85% Komödie
    5461.0h  0.83% Quiz
    4958.7h  0.75% Wissensmagazin
    4832.1h  0.73% Wirtschaftsmagazin
    4804.0h  0.73% Realityshow
    4702.9h  0.71% Telenovela
    4669.4h  0.71% Musikmagazin
    4660.1h  0.71% Politikmagazin
