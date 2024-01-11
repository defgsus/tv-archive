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

**98** channels, **645,328.7** hours playtime between **2023-01-17** and **2024-01-12**


### playtime per genre (top 30)

    42130.8h 6.53% Nachrichten
    30829.2h 4.78% Verkaufsshow
    25892.5h 4.01% Krimiserie
    21966.3h 3.40% Werbesendung
    20962.5h 3.25% Dokureihe
    19283.0h 2.99% Dokusoap
    18562.9h 2.88% Regionalmagazin
    16774.8h 2.60% Dokumentation
    16064.6h 2.49% *unknown*
    11917.3h 1.85% Zeichentrickserie
    11705.1h 1.81% Infomercial
    11343.1h 1.76% Animationsserie
    9786.3h  1.52% Comedyserie
    9135.9h  1.42% Morgenmagazin
    8726.9h  1.35% Religionsmagazin
    8510.9h  1.32% Talkshow
    8493.4h  1.32% Magazin
    6347.8h  0.98% E-Sport
    6280.8h  0.97% Programmende
    6247.4h  0.97% Sitcom
    5855.8h  0.91% Wetterbericht
    5757.1h  0.89% Börsenmagazin
    5466.3h  0.85% Komödie
    5326.0h  0.83% Quiz
    4859.9h  0.75% Wissensmagazin
    4740.6h  0.73% Wirtschaftsmagazin
    4700.3h  0.73% Realityshow
    4600.3h  0.71% Telenovela
    4599.1h  0.71% Musikmagazin
    4548.1h  0.70% Politikmagazin
