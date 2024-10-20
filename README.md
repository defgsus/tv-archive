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

**109** channels, **1,099,778.1** hours playtime between **2023-01-17** and **2024-10-21**


### playtime per genre (top 30)

    71566.5h 6.51% Nachrichten
    50705.5h 4.61% Verkaufsshow
    45618.8h 4.15% Krimiserie
    40225.6h 3.66% Werbesendung
    34440.0h 3.13% Dokureihe
    32922.6h 2.99% Dokusoap
    32121.2h 2.92% Regionalmagazin
    28817.7h 2.62% Dokumentation
    26192.9h 2.38% *unknown*
    20501.2h 1.86% Zeichentrickserie
    20233.2h 1.84% Infomercial
    19684.9h 1.79% Animationsserie
    15908.2h 1.45% Comedyserie
    15370.5h 1.40% Morgenmagazin
    14850.8h 1.35% Religionsmagazin
    14542.5h 1.32% Talkshow
    14013.6h 1.27% Magazin
    10874.3h 0.99% E-Sport
    10577.9h 0.96% Sitcom
    9959.9h  0.91% Wetterbericht
    9776.6h  0.89% Programmende
    9656.6h  0.88% Komödie
    9629.8h  0.88% Quiz
    8410.8h  0.76% Börsenmagazin
    8354.1h  0.76% Realityshow
    8298.4h  0.75% Politikmagazin
    8271.2h  0.75% Wissensmagazin
    7399.5h  0.67% Wirtschaftsmagazin
    7237.4h  0.66% Telenovela
    7179.4h  0.65% Dramaserie
