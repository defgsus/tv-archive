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

**109** channels, **1,034,276.1** hours playtime between **2023-01-17** and **2024-09-08**


### playtime per genre (top 30)

    67284.4h 6.51% Nachrichten
    48076.5h 4.65% Verkaufsshow
    42607.7h 4.12% Krimiserie
    37429.2h 3.62% Werbesendung
    32512.2h 3.14% Dokureihe
    31185.7h 3.02% Dokusoap
    30167.1h 2.92% Regionalmagazin
    27060.3h 2.62% Dokumentation
    25023.5h 2.42% *unknown*
    19194.0h 1.86% Zeichentrickserie
    18962.2h 1.83% Infomercial
    18532.1h 1.79% Animationsserie
    15146.8h 1.46% Comedyserie
    14486.2h 1.40% Morgenmagazin
    14056.6h 1.36% Religionsmagazin
    13599.0h 1.31% Magazin
    13580.4h 1.31% Talkshow
    10214.9h 0.99% E-Sport
    9893.5h  0.96% Sitcom
    9358.6h  0.90% Wetterbericht
    9278.0h  0.90% Programmende
    9094.9h  0.88% Komödie
    8936.9h  0.86% Quiz
    8213.5h  0.79% Börsenmagazin
    7736.4h  0.75% Wissensmagazin
    7729.0h  0.75% Politikmagazin
    7702.2h  0.74% Realityshow
    7036.9h  0.68% Wirtschaftsmagazin
    6805.7h  0.66% Telenovela
    6734.8h  0.65% Dramaserie
