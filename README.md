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

**109** channels, **1,039,688.1** hours playtime between **2023-01-17** and **2024-09-11**


### playtime per genre (top 30)

    67632.9h 6.51% Nachrichten
    48298.8h 4.65% Verkaufsshow
    42863.6h 4.12% Krimiserie
    37651.6h 3.62% Werbesendung
    32661.5h 3.14% Dokureihe
    31330.4h 3.01% Dokusoap
    30344.7h 2.92% Regionalmagazin
    27189.2h 2.62% Dokumentation
    25080.2h 2.41% *unknown*
    19295.8h 1.86% Zeichentrickserie
    19064.7h 1.83% Infomercial
    18627.0h 1.79% Animationsserie
    15213.2h 1.46% Comedyserie
    14556.4h 1.40% Morgenmagazin
    14140.6h 1.36% Religionsmagazin
    13653.2h 1.31% Talkshow
    13622.1h 1.31% Magazin
    10269.6h 0.99% E-Sport
    9946.3h  0.96% Sitcom
    9406.4h  0.90% Wetterbericht
    9318.7h  0.90% Programmende
    9136.3h  0.88% Komödie
    8995.2h  0.87% Quiz
    8230.0h  0.79% Börsenmagazin
    7785.9h  0.75% Politikmagazin
    7785.3h  0.75% Wissensmagazin
    7744.1h  0.74% Realityshow
    7069.1h  0.68% Wirtschaftsmagazin
    6841.2h  0.66% Telenovela
    6758.1h  0.65% Dramaserie
