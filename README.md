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

**109** channels, **966,827.6** hours playtime between **2023-01-17** and **2024-07-27**


### playtime per genre (top 30)

    62983.8h 6.51% Nachrichten
    45131.9h 4.67% Verkaufsshow
    39667.4h 4.10% Krimiserie
    34588.2h 3.58% Werbesendung
    30384.3h 3.14% Dokureihe
    29289.9h 3.03% Dokusoap
    28156.8h 2.91% Regionalmagazin
    25143.2h 2.60% Dokumentation
    24029.7h 2.49% *unknown*
    17897.8h 1.85% Zeichentrickserie
    17675.3h 1.83% Infomercial
    17296.4h 1.79% Animationsserie
    14359.8h 1.49% Comedyserie
    13623.9h 1.41% Morgenmagazin
    13418.1h 1.39% Magazin
    13122.4h 1.36% Religionsmagazin
    12766.7h 1.32% Talkshow
    9586.1h  0.99% E-Sport
    9135.5h  0.94% Sitcom
    8759.5h  0.91% Programmende
    8682.6h  0.90% Wetterbericht
    8428.6h  0.87% Komödie
    8343.8h  0.86% Quiz
    8002.2h  0.83% Börsenmagazin
    7281.4h  0.75% Politikmagazin
    7181.7h  0.74% Wissensmagazin
    7175.6h  0.74% Realityshow
    6687.5h  0.69% Wirtschaftsmagazin
    6464.1h  0.67% Telenovela
    6311.0h  0.65% Dramaserie
