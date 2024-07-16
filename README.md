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

**109** channels, **952,401.1** hours playtime between **2023-01-17** and **2024-07-17**


### playtime per genre (top 30)

    62043.6h 6.51% Nachrichten
    44496.8h 4.67% Verkaufsshow
    39008.8h 4.10% Krimiserie
    33977.8h 3.57% Werbesendung
    29968.2h 3.15% Dokureihe
    28824.9h 3.03% Dokusoap
    27704.8h 2.91% Regionalmagazin
    24704.1h 2.59% Dokumentation
    23761.6h 2.49% *unknown*
    17590.4h 1.85% Zeichentrickserie
    17397.9h 1.83% Infomercial
    17036.8h 1.79% Animationsserie
    14173.9h 1.49% Comedyserie
    13411.1h 1.41% Morgenmagazin
    13382.9h 1.41% Magazin
    12919.8h 1.36% Religionsmagazin
    12599.7h 1.32% Talkshow
    9427.2h  0.99% E-Sport
    8973.4h  0.94% Sitcom
    8653.1h  0.91% Programmende
    8532.9h  0.90% Wetterbericht
    8298.0h  0.87% Komödie
    8224.1h  0.86% Quiz
    7948.9h  0.83% Börsenmagazin
    7178.2h  0.75% Politikmagazin
    7079.1h  0.74% Realityshow
    7075.5h  0.74% Wissensmagazin
    6608.3h  0.69% Wirtschaftsmagazin
    6412.4h  0.67% Telenovela
    6196.4h  0.65% Dramaserie
