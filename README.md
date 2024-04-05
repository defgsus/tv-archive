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

**102** channels, **794,177.2** hours playtime between **2023-01-17** and **2024-04-06**


### playtime per genre (top 30)

    51684.6h 6.51% Nachrichten
    38113.1h 4.80% Verkaufsshow
    32330.6h 4.07% Krimiserie
    27671.2h 3.48% Werbesendung
    25230.5h 3.18% Dokureihe
    23917.9h 3.01% Dokusoap
    23078.6h 2.91% Regionalmagazin
    20563.4h 2.59% Dokumentation
    20400.7h 2.57% *unknown*
    14592.7h 1.84% Zeichentrickserie
    14405.4h 1.81% Infomercial
    14092.2h 1.77% Animationsserie
    12035.0h 1.52% Comedyserie
    11235.2h 1.41% Morgenmagazin
    10975.7h 1.38% Magazin
    10724.1h 1.35% Religionsmagazin
    10570.3h 1.33% Talkshow
    7824.8h  0.99% E-Sport
    7440.8h  0.94% Programmende
    7371.6h  0.93% Sitcom
    7048.1h  0.89% Wetterbericht
    7022.2h  0.88% Börsenmagazin
    6804.6h  0.86% Quiz
    6795.6h  0.86% Komödie
    5904.0h  0.74% Wissensmagazin
    5767.9h  0.73% Politikmagazin
    5707.6h  0.72% Realityshow
    5703.5h  0.72% Wirtschaftsmagazin
    5671.7h  0.71% Telenovela
    5349.8h  0.67% Musikmagazin
