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

**96** channels, **159,292.5** hours playtime between **2023-01-17** and **2023-04-15**


### playtime per genre (top 30)

    10965.1h 6.88% Nachrichten
    7884.0h  4.95% Verkaufsshow
    6555.0h  4.12% Krimiserie
    5327.3h  3.34% Werbesendung
    5125.8h  3.22% Dokureihe
    4805.7h  3.02% Dokusoap
    4647.4h  2.92% Regionalmagazin
    4009.8h  2.52% Dokumentation
    3750.5h  2.35% *unknown*
    2955.4h  1.86% Animationsserie
    2917.3h  1.83% Zeichentrickserie
    2900.0h  1.82% Infomercial
    2628.1h  1.65% Comedyserie
    2232.8h  1.40% Morgenmagazin
    2198.5h  1.38% Programmende
    2067.9h  1.30% Religionsmagazin
    2052.1h  1.29% Talkshow
    1712.9h  1.08% Magazin
    1640.1h  1.03% E-Sport
    1505.3h  0.94% Sitcom
    1481.8h  0.93% Börsenmagazin
    1435.9h  0.90% Wetterbericht
    1289.7h  0.81% Wirtschaftsmagazin
    1245.7h  0.78% Wissensmagazin
    1207.8h  0.76% Quiz
    1207.6h  0.76% Musikmagazin
    1111.4h  0.70% Telenovela
    1101.1h  0.69% Dramaserie
    1101.0h  0.69% Gesundheitsmagazin
    1081.6h  0.68% Sportmagazin
