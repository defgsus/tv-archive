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

**102** channels, **810,630.6** hours playtime between **2023-01-17** and **2024-04-16**


### playtime per genre (top 30)

    52752.0h 6.51% Nachrichten
    38913.8h 4.80% Verkaufsshow
    32989.2h 4.07% Krimiserie
    28286.1h 3.49% Werbesendung
    25692.7h 3.17% Dokureihe
    24437.8h 3.01% Dokusoap
    23550.5h 2.91% Regionalmagazin
    21012.3h 2.59% Dokumentation
    20804.4h 2.57% *unknown*
    14881.0h 1.84% Zeichentrickserie
    14714.5h 1.82% Infomercial
    14410.4h 1.78% Animationsserie
    12290.2h 1.52% Comedyserie
    11438.5h 1.41% Morgenmagazin
    11254.1h 1.39% Magazin
    10940.0h 1.35% Religionsmagazin
    10788.4h 1.33% Talkshow
    7994.6h  0.99% E-Sport
    7566.0h  0.93% Programmende
    7489.9h  0.92% Sitcom
    7192.1h  0.89% Wetterbericht
    7138.6h  0.88% Börsenmagazin
    6988.9h  0.86% Quiz
    6936.8h  0.86% Komödie
    6014.0h  0.74% Wissensmagazin
    5906.4h  0.73% Politikmagazin
    5834.3h  0.72% Realityshow
    5807.7h  0.72% Wirtschaftsmagazin
    5786.8h  0.71% Telenovela
    5428.9h  0.67% Musikmagazin
