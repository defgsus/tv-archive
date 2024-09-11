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

**109** channels, **1,041,550.2** hours playtime between **2023-01-17** and **2024-09-12**


### playtime per genre (top 30)

    67769.8h 6.51% Nachrichten
    48398.1h 4.65% Verkaufsshow
    42941.7h 4.12% Krimiserie
    37728.8h 3.62% Werbesendung
    32703.6h 3.14% Dokureihe
    31377.4h 3.01% Dokusoap
    30420.7h 2.92% Regionalmagazin
    27247.7h 2.62% Dokumentation
    25122.5h 2.41% *unknown*
    19331.8h 1.86% Zeichentrickserie
    19098.9h 1.83% Infomercial
    18660.0h 1.79% Animationsserie
    15241.6h 1.46% Comedyserie
    14590.8h 1.40% Morgenmagazin
    14161.0h 1.36% Religionsmagazin
    13687.5h 1.31% Talkshow
    13629.1h 1.31% Magazin
    10293.4h 0.99% E-Sport
    9973.5h  0.96% Sitcom
    9424.9h  0.90% Wetterbericht
    9332.3h  0.90% Programmende
    9146.7h  0.88% Komödie
    9017.4h  0.87% Quiz
    8239.0h  0.79% Börsenmagazin
    7808.7h  0.75% Politikmagazin
    7800.8h  0.75% Wissensmagazin
    7761.6h  0.75% Realityshow
    7084.2h  0.68% Wirtschaftsmagazin
    6860.4h  0.66% Telenovela
    6777.3h  0.65% Dramaserie
