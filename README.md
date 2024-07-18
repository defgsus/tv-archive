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

**109** channels, **956,021.7** hours playtime between **2023-01-17** and **2024-07-19**


### playtime per genre (top 30)

    62299.8h 6.52% Nachrichten
    44662.5h 4.67% Verkaufsshow
    39177.8h 4.10% Krimiserie
    34124.2h 3.57% Werbesendung
    30076.8h 3.15% Dokureihe
    28939.2h 3.03% Dokusoap
    27836.7h 2.91% Regionalmagazin
    24802.9h 2.59% Dokumentation
    23830.3h 2.49% *unknown*
    17659.8h 1.85% Zeichentrickserie
    17466.1h 1.83% Infomercial
    17103.3h 1.79% Animationsserie
    14224.7h 1.49% Comedyserie
    13479.7h 1.41% Morgenmagazin
    13394.5h 1.40% Magazin
    12966.3h 1.36% Religionsmagazin
    12642.5h 1.32% Talkshow
    9462.5h  0.99% E-Sport
    9021.0h  0.94% Sitcom
    8682.3h  0.91% Programmende
    8568.4h  0.90% Wetterbericht
    8315.6h  0.87% Komödie
    8251.8h  0.86% Quiz
    7966.2h  0.83% Börsenmagazin
    7219.5h  0.76% Politikmagazin
    7111.4h  0.74% Wissensmagazin
    7107.4h  0.74% Realityshow
    6634.9h  0.69% Wirtschaftsmagazin
    6425.9h  0.67% Telenovela
    6243.8h  0.65% Dramaserie
