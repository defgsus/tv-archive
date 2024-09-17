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

**109** channels, **1,050,715.6** hours playtime between **2023-01-17** and **2024-09-18**


### playtime per genre (top 30)

    68352.3h 6.51% Nachrichten
    48768.4h 4.64% Verkaufsshow
    43365.9h 4.13% Krimiserie
    38109.5h 3.63% Werbesendung
    32998.0h 3.14% Dokureihe
    31634.5h 3.01% Dokusoap
    30684.5h 2.92% Regionalmagazin
    27488.2h 2.62% Dokumentation
    25281.7h 2.41% *unknown*
    19496.8h 1.86% Zeichentrickserie
    19282.1h 1.84% Infomercial
    18819.5h 1.79% Animationsserie
    15356.9h 1.46% Comedyserie
    14711.7h 1.40% Morgenmagazin
    14294.7h 1.36% Religionsmagazin
    13826.1h 1.32% Talkshow
    13686.4h 1.30% Magazin
    10388.1h 0.99% E-Sport
    10063.5h 0.96% Sitcom
    9511.1h  0.91% Wetterbericht
    9402.1h  0.89% Programmende
    9232.1h  0.88% Komödie
    9116.4h  0.87% Quiz
    8264.7h  0.79% Börsenmagazin
    7878.0h  0.75% Wissensmagazin
    7876.1h  0.75% Politikmagazin
    7837.1h  0.75% Realityshow
    7131.8h  0.68% Wirtschaftsmagazin
    6917.7h  0.66% Telenovela
    6835.0h  0.65% Dramaserie
