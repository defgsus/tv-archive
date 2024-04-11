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

**102** channels, **804,824.5** hours playtime between **2023-01-17** and **2024-04-12**


### playtime per genre (top 30)

    52386.6h 6.51% Nachrichten
    38629.5h 4.80% Verkaufsshow
    32760.7h 4.07% Krimiserie
    28070.6h 3.49% Werbesendung
    25527.1h 3.17% Dokureihe
    24249.5h 3.01% Dokusoap
    23393.1h 2.91% Regionalmagazin
    20842.0h 2.59% Dokumentation
    20692.9h 2.57% *unknown*
    14779.7h 1.84% Zeichentrickserie
    14603.4h 1.81% Infomercial
    14296.9h 1.78% Animationsserie
    12201.5h 1.52% Comedyserie
    11368.7h 1.41% Morgenmagazin
    11168.5h 1.39% Magazin
    10870.7h 1.35% Religionsmagazin
    10709.9h 1.33% Talkshow
    7918.3h  0.98% E-Sport
    7523.9h  0.93% Programmende
    7452.3h  0.93% Sitcom
    7144.2h  0.89% Wetterbericht
    7100.9h  0.88% Börsenmagazin
    6917.7h  0.86% Quiz
    6893.4h  0.86% Komödie
    5972.1h  0.74% Wissensmagazin
    5863.2h  0.73% Politikmagazin
    5796.1h  0.72% Realityshow
    5771.0h  0.72% Wirtschaftsmagazin
    5748.8h  0.71% Telenovela
    5405.9h  0.67% Musikmagazin
