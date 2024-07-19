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

**109** channels, **956,024.6** hours playtime between **2023-01-17** and **2024-07-20**


### playtime per genre (top 30)

    62294.9h 6.52% Nachrichten
    44666.2h 4.67% Verkaufsshow
    39179.0h 4.10% Krimiserie
    34121.7h 3.57% Werbesendung
    30037.9h 3.14% Dokureihe
    28951.9h 3.03% Dokusoap
    27834.3h 2.91% Regionalmagazin
    24799.5h 2.59% Dokumentation
    23837.2h 2.49% *unknown*
    17682.7h 1.85% Zeichentrickserie
    17467.4h 1.83% Infomercial
    17096.8h 1.79% Animationsserie
    14220.8h 1.49% Comedyserie
    13479.8h 1.41% Morgenmagazin
    13392.3h 1.40% Magazin
    12964.6h 1.36% Religionsmagazin
    12646.8h 1.32% Talkshow
    9463.0h  0.99% E-Sport
    9017.6h  0.94% Sitcom
    8682.8h  0.91% Programmende
    8569.1h  0.90% Wetterbericht
    8316.1h  0.87% Komödie
    8251.5h  0.86% Quiz
    7966.4h  0.83% Börsenmagazin
    7209.7h  0.75% Politikmagazin
    7104.5h  0.74% Realityshow
    7099.0h  0.74% Wissensmagazin
    6635.3h  0.69% Wirtschaftsmagazin
    6429.4h  0.67% Telenovela
    6233.4h  0.65% Dramaserie
