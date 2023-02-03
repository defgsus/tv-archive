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

**96** channels, **33,744.6** hours playtime between **2023-01-17** and **2023-02-04**


### playtime per genre (top 30)

    2407.8h 7.14% Nachrichten
    1784.9h 5.29% Verkaufsshow
    1435.0h 4.25% Krimiserie
    1198.5h 3.55% Dokusoap
    1127.1h 3.34% Werbesendung
    1016.7h 3.01% Dokureihe
    1004.5h 2.98% Regionalmagazin
    845.4h  2.51% Dokumentation
    827.6h  2.45% *unknown*
    655.0h  1.94% Zeichentrickserie
    640.2h  1.90% Infomercial
    598.4h  1.77% Animationsserie
    583.8h  1.73% Comedyserie
    489.0h  1.45% Morgenmagazin
    439.3h  1.30% Talkshow
    438.2h  1.30% Religionsmagazin
    419.1h  1.24% Programmende
    393.9h  1.17% Magazin
    363.6h  1.08% E-Sport
    314.7h  0.93% Sitcom
    301.2h  0.89% Börsenmagazin
    289.2h  0.86% Wirtschaftsmagazin
    288.0h  0.85% Wetterbericht
    275.0h  0.81% Wissensmagazin
    271.4h  0.80% Quiz
    268.3h  0.80% Dramaserie
    253.3h  0.75% Musikmagazin
    250.9h  0.74% Telenovela
    241.5h  0.72% Gesundheitsmagazin
    232.0h  0.69% Realityshow
