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

**109** channels, **1,045,197.1** hours playtime between **2023-01-17** and **2024-09-15**


### playtime per genre (top 30)

    67987.6h 6.50% Nachrichten
    48536.1h 4.64% Verkaufsshow
    43103.7h 4.12% Krimiserie
    37873.5h 3.62% Werbesendung
    32817.7h 3.14% Dokureihe
    31484.7h 3.01% Dokusoap
    30508.2h 2.92% Regionalmagazin
    27333.6h 2.62% Dokumentation
    25181.4h 2.41% *unknown*
    19398.2h 1.86% Zeichentrickserie
    19171.0h 1.83% Infomercial
    18729.9h 1.79% Animationsserie
    15283.9h 1.46% Comedyserie
    14632.2h 1.40% Morgenmagazin
    14204.5h 1.36% Religionsmagazin
    13742.2h 1.31% Talkshow
    13645.9h 1.31% Magazin
    10327.6h 0.99% E-Sport
    10009.6h 0.96% Sitcom
    9456.7h  0.90% Wetterbericht
    9355.6h  0.90% Programmende
    9184.0h  0.88% Komödie
    9064.7h  0.87% Quiz
    8247.5h  0.79% Börsenmagazin
    7827.1h  0.75% Wissensmagazin
    7823.8h  0.75% Politikmagazin
    7787.6h  0.75% Realityshow
    7101.8h  0.68% Wirtschaftsmagazin
    6880.1h  0.66% Telenovela
    6799.1h  0.65% Dramaserie
