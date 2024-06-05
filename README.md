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

**108** channels, **888,934.4** hours playtime between **2023-01-17** and **2024-06-06**


### playtime per genre (top 30)

    58109.6h 6.54% Nachrichten
    42040.7h 4.73% Verkaufsshow
    36169.7h 4.07% Krimiserie
    31282.9h 3.52% Werbesendung
    27988.0h 3.15% Dokureihe
    26885.9h 3.02% Dokusoap
    25856.0h 2.91% Regionalmagazin
    23079.6h 2.60% Dokumentation
    22456.6h 2.53% *unknown*
    16346.6h 1.84% Zeichentrickserie
    16181.5h 1.82% Infomercial
    15846.9h 1.78% Animationsserie
    13330.9h 1.50% Comedyserie
    12684.1h 1.43% Magazin
    12513.3h 1.41% Morgenmagazin
    12032.1h 1.35% Religionsmagazin
    11836.7h 1.33% Talkshow
    8804.4h  0.99% E-Sport
    8264.2h  0.93% Sitcom
    8172.1h  0.92% Programmende
    7921.1h  0.89% Wetterbericht
    7750.5h  0.87% Börsenmagazin
    7707.4h  0.87% Quiz
    7662.6h  0.86% Komödie
    6602.9h  0.74% Politikmagazin
    6586.8h  0.74% Wissensmagazin
    6571.3h  0.74% Realityshow
    6286.5h  0.71% Wirtschaftsmagazin
    6222.5h  0.70% Telenovela
    5870.0h  0.66% Musikmagazin
