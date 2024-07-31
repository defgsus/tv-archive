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

**109** channels, **975,938.7** hours playtime between **2023-01-17** and **2024-08-01**


### playtime per genre (top 30)

    63532.7h 6.51% Nachrichten
    45544.2h 4.67% Verkaufsshow
    40016.7h 4.10% Krimiserie
    34983.2h 3.58% Werbesendung
    30687.3h 3.14% Dokureihe
    29538.9h 3.03% Dokusoap
    28413.2h 2.91% Regionalmagazin
    25406.8h 2.60% Dokumentation
    24131.6h 2.47% *unknown*
    18076.4h 1.85% Zeichentrickserie
    17848.5h 1.83% Infomercial
    17461.0h 1.79% Animationsserie
    14452.2h 1.48% Comedyserie
    13726.0h 1.41% Morgenmagazin
    13440.8h 1.38% Magazin
    13258.2h 1.36% Religionsmagazin
    12860.5h 1.32% Talkshow
    9660.1h  0.99% E-Sport
    9240.4h  0.95% Sitcom
    8828.0h  0.90% Programmende
    8770.0h  0.90% Wetterbericht
    8530.3h  0.87% Komödie
    8409.5h  0.86% Quiz
    8029.0h  0.82% Börsenmagazin
    7342.3h  0.75% Politikmagazin
    7257.0h  0.74% Wissensmagazin
    7227.1h  0.74% Realityshow
    6729.9h  0.69% Wirtschaftsmagazin
    6485.0h  0.66% Telenovela
    6365.1h  0.65% Dramaserie
