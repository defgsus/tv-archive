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

**109** channels, **912,542.6** hours playtime between **2023-01-17** and **2024-06-22**


### playtime per genre (top 30)

    59644.0h 6.54% Nachrichten
    42945.5h 4.71% Verkaufsshow
    37212.7h 4.08% Krimiserie
    32265.9h 3.54% Werbesendung
    28683.5h 3.14% Dokureihe
    27597.6h 3.02% Dokusoap
    26565.4h 2.91% Regionalmagazin
    23695.9h 2.60% Dokumentation
    22913.2h 2.51% *unknown*
    16786.6h 1.84% Zeichentrickserie
    16631.8h 1.82% Infomercial
    16291.9h 1.79% Animationsserie
    13660.9h 1.50% Comedyserie
    13019.3h 1.43% Magazin
    12868.0h 1.41% Morgenmagazin
    12355.8h 1.35% Religionsmagazin
    12157.8h 1.33% Talkshow
    9019.9h  0.99% E-Sport
    8535.5h  0.94% Sitcom
    8351.3h  0.92% Programmende
    8147.6h  0.89% Wetterbericht
    7892.4h  0.86% Komödie
    7890.9h  0.86% Quiz
    7827.0h  0.86% Börsenmagazin
    6859.8h  0.75% Politikmagazin
    6769.9h  0.74% Wissensmagazin
    6768.1h  0.74% Realityshow
    6411.0h  0.70% Wirtschaftsmagazin
    6303.2h  0.69% Telenovela
    5990.9h  0.66% Musikmagazin
