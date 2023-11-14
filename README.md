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

**97** channels, **543,476.1** hours playtime between **2023-01-17** and **2023-11-15**


### playtime per genre (top 30)

    35762.8h 6.58% Nachrichten
    25961.8h 4.78% Verkaufsshow
    21897.6h 4.03% Krimiserie
    18432.5h 3.39% Werbesendung
    17759.2h 3.27% Dokureihe
    16496.0h 3.04% Dokusoap
    15696.7h 2.89% Regionalmagazin
    13853.9h 2.55% Dokumentation
    13200.4h 2.43% *unknown*
    10082.7h 1.86% Zeichentrickserie
    9902.9h  1.82% Infomercial
    9707.8h  1.79% Animationsserie
    8539.6h  1.57% Comedyserie
    7728.4h  1.42% Morgenmagazin
    7329.6h  1.35% Religionsmagazin
    7262.3h  1.34% Talkshow
    6910.1h  1.27% Magazin
    5498.9h  1.01% Programmende
    5327.8h  0.98% E-Sport
    5208.0h  0.96% Sitcom
    5002.8h  0.92% Wetterbericht
    4930.3h  0.91% Börsenmagazin
    4534.8h  0.83% Quiz
    4246.1h  0.78% Komödie
    4114.6h  0.76% Wissensmagazin
    4085.2h  0.75% Wirtschaftsmagazin
    4021.8h  0.74% Musikmagazin
    3916.8h  0.72% Telenovela
    3773.7h  0.69% Politikmagazin
    3721.2h  0.68% Realityshow
