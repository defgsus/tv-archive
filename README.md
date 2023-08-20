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

**97** channels, **389,547.9** hours playtime between **2023-01-17** and **2023-08-21**


### playtime per genre (top 30)

    25723.5h 6.60% Nachrichten
    18366.2h 4.71% Verkaufsshow
    15773.0h 4.05% Krimiserie
    13127.2h 3.37% Werbesendung
    12919.0h 3.32% Dokureihe
    11773.0h 3.02% Dokusoap
    11148.3h 2.86% Regionalmagazin
    9852.0h  2.53% Dokumentation
    9479.4h  2.43% *unknown*
    7356.9h  1.89% Zeichentrickserie
    7115.1h  1.83% Infomercial
    6880.4h  1.77% Animationsserie
    6350.4h  1.63% Comedyserie
    5465.1h  1.40% Morgenmagazin
    5196.0h  1.33% Religionsmagazin
    5130.4h  1.32% Talkshow
    4852.6h  1.25% Magazin
    4316.3h  1.11% Programmende
    3858.1h  0.99% E-Sport
    3678.2h  0.94% Wetterbericht
    3643.6h  0.94% Sitcom
    3500.1h  0.90% Börsenmagazin
    3135.7h  0.80% Quiz
    3073.7h  0.79% Musikmagazin
    3024.8h  0.78% Komödie
    2966.8h  0.76% Wirtschaftsmagazin
    2917.0h  0.75% Wissensmagazin
    2705.2h  0.69% Telenovela
    2569.5h  0.66% Reportagereihe
    2508.5h  0.64% Sportmagazin
