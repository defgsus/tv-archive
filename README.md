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

**96** channels, **4,086.0** hours playtime between **2023-01-17** and **2023-01-19**


### playtime per genre (top 30)

    322.8h 7.90% Nachrichten
    247.5h 6.06% Verkaufsshow
    180.6h 4.42% Krimiserie
    137.8h 3.37% *unknown*
    132.1h 3.23% Regionalmagazin
    130.7h 3.20% Werbesendung
    128.3h 3.14% Dokureihe
    126.7h 3.10% Dokusoap
    95.6h  2.34% Infomercial
    93.9h  2.30% Comedyserie
    87.0h  2.13% Dokumentation
    80.5h  1.97% Zeichentrickserie
    67.4h  1.65% Animationsserie
    59.3h  1.45% Magazin
    54.8h  1.34% Talkshow
    53.6h  1.31% Religionsmagazin
    53.4h  1.31% E-Sport
    48.2h  1.18% Morgenmagazin
    42.3h  1.04% Börsenmagazin
    39.9h  0.98% Sitcom
    38.9h  0.95% Wirtschaftsmagazin
    38.8h  0.95% Tennis
    38.0h  0.93% Krankenhausserie
    35.3h  0.86% Realityshow
    34.9h  0.85% Musikmagazin
    33.4h  0.82% Gerichtsshow
    33.3h  0.82% Gesundheitsmagazin
    33.2h  0.81% Dramaserie
    32.1h  0.79% Telenovela
    29.6h  0.72% Wetterbericht
