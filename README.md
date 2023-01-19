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

**96** channels, **6,388.7** hours playtime between **2023-01-17** and **2023-01-20**


### playtime per genre (top 30)

    499.0h 7.81% Nachrichten
    383.5h 6.00% Verkaufsshow
    275.6h 4.31% Krimiserie
    223.7h 3.50% Dokusoap
    218.9h 3.43% Regionalmagazin
    206.5h 3.23% *unknown*
    197.0h 3.08% Dokureihe
    191.2h 2.99% Werbesendung
    146.8h 2.30% Infomercial
    136.2h 2.13% Dokumentation
    131.5h 2.06% Comedyserie
    118.5h 1.86% Zeichentrickserie
    103.4h 1.62% Animationsserie
    93.1h  1.46% Talkshow
    91.6h  1.43% Magazin
    82.5h  1.29% Morgenmagazin
    81.6h  1.28% Religionsmagazin
    75.2h  1.18% E-Sport
    60.2h  0.94% Wirtschaftsmagazin
    59.1h  0.92% Sitcom
    55.2h  0.86% Tennis
    54.6h  0.85% Krankenhausserie
    54.2h  0.85% Musikmagazin
    54.1h  0.85% Realityshow
    53.0h  0.83% Börsenmagazin
    51.6h  0.81% Telenovela
    49.2h  0.77% Gerichtsshow
    49.0h  0.77% Wissensmagazin
    49.0h  0.77% Gesundheitsmagazin
    48.6h  0.76% Dramaserie
