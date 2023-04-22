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

**96** channels, **173,926.9** hours playtime between **2023-01-17** and **2023-04-23**


### playtime per genre (top 30)

    11867.0h 6.82% Nachrichten
    8584.2h  4.94% Verkaufsshow
    7142.7h  4.11% Krimiserie
    5812.0h  3.34% Werbesendung
    5609.6h  3.23% Dokureihe
    5175.9h  2.98% Dokusoap
    5040.2h  2.90% Regionalmagazin
    4372.7h  2.51% Dokumentation
    4165.5h  2.39% *unknown*
    3204.5h  1.84% Zeichentrickserie
    3202.6h  1.84% Animationsserie
    3179.5h  1.83% Infomercial
    2870.2h  1.65% Comedyserie
    2414.9h  1.39% Morgenmagazin
    2407.7h  1.38% Programmende
    2258.5h  1.30% Talkshow
    2257.6h  1.30% Religionsmagazin
    1905.8h  1.10% Magazin
    1773.5h  1.02% E-Sport
    1642.5h  0.94% Sitcom
    1591.9h  0.92% Börsenmagazin
    1571.8h  0.90% Wetterbericht
    1389.7h  0.80% Wirtschaftsmagazin
    1361.0h  0.78% Wissensmagazin
    1326.3h  0.76% Musikmagazin
    1322.3h  0.76% Quiz
    1217.4h  0.70% Telenovela
    1204.4h  0.69% Gesundheitsmagazin
    1195.4h  0.69% Sportmagazin
    1181.8h  0.68% Dramaserie
