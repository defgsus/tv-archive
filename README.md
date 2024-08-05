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

**109** channels, **983,162.2** hours playtime between **2023-01-17** and **2024-08-06**


### playtime per genre (top 30)

    63952.5h 6.50% Nachrichten
    45852.2h 4.66% Verkaufsshow
    40295.0h 4.10% Krimiserie
    35280.9h 3.59% Werbesendung
    30923.8h 3.15% Dokureihe
    29740.4h 3.02% Dokusoap
    28600.8h 2.91% Regionalmagazin
    25584.1h 2.60% Dokumentation
    24224.2h 2.46% *unknown*
    18220.8h 1.85% Zeichentrickserie
    17989.3h 1.83% Infomercial
    17584.6h 1.79% Animationsserie
    14527.1h 1.48% Comedyserie
    13797.4h 1.40% Morgenmagazin
    13452.2h 1.37% Magazin
    13365.1h 1.36% Religionsmagazin
    12936.9h 1.32% Talkshow
    9731.8h  0.99% E-Sport
    9322.3h  0.95% Sitcom
    8883.3h  0.90% Programmende
    8842.5h  0.90% Wetterbericht
    8615.6h  0.88% Komödie
    8459.2h  0.86% Quiz
    8046.7h  0.82% Börsenmagazin
    7375.8h  0.75% Politikmagazin
    7313.2h  0.74% Wissensmagazin
    7276.1h  0.74% Realityshow
    6759.7h  0.69% Wirtschaftsmagazin
    6501.4h  0.66% Telenovela
    6394.5h  0.65% Dramaserie
