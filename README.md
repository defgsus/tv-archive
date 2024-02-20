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

**99** channels, **716,376.4** hours playtime between **2023-01-17** and **2024-02-21**


### playtime per genre (top 30)

    46647.7h 6.51% Nachrichten
    34394.8h 4.80% Verkaufsshow
    29037.2h 4.05% Krimiserie
    24680.3h 3.45% Werbesendung
    22982.5h 3.21% Dokureihe
    21588.8h 3.01% Dokusoap
    20743.5h 2.90% Regionalmagazin
    18490.6h 2.58% Dokumentation
    18168.1h 2.54% *unknown*
    13289.1h 1.86% Zeichentrickserie
    13022.4h 1.82% Infomercial
    12598.2h 1.76% Animationsserie
    10848.6h 1.51% Comedyserie
    10150.5h 1.42% Morgenmagazin
    9691.9h  1.35% Religionsmagazin
    9577.7h  1.34% Magazin
    9497.4h  1.33% Talkshow
    7066.5h  0.99% E-Sport
    6833.4h  0.95% Programmende
    6798.9h  0.95% Sitcom
    6393.6h  0.89% Börsenmagazin
    6372.2h  0.89% Wetterbericht
    6084.0h  0.85% Komödie
    5989.9h  0.84% Quiz
    5369.9h  0.75% Wissensmagazin
    5256.7h  0.73% Realityshow
    5197.9h  0.73% Wirtschaftsmagazin
    5139.5h  0.72% Politikmagazin
    5105.6h  0.71% Telenovela
    4955.6h  0.69% Musikmagazin
