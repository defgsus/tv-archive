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

**96** channels, **159,295.2** hours playtime between **2023-01-17** and **2023-04-15**


### playtime per genre (top 30)

    10965.5h 6.88% Nachrichten
    7885.4h  4.95% Verkaufsshow
    6554.9h  4.11% Krimiserie
    5327.3h  3.34% Werbesendung
    5124.7h  3.22% Dokureihe
    4806.0h  3.02% Dokusoap
    4647.4h  2.92% Regionalmagazin
    4010.2h  2.52% Dokumentation
    3751.8h  2.36% *unknown*
    2955.2h  1.86% Animationsserie
    2917.0h  1.83% Zeichentrickserie
    2900.0h  1.82% Infomercial
    2628.3h  1.65% Comedyserie
    2232.8h  1.40% Morgenmagazin
    2198.6h  1.38% Programmende
    2067.9h  1.30% Religionsmagazin
    2052.2h  1.29% Talkshow
    1712.0h  1.07% Magazin
    1640.1h  1.03% E-Sport
    1505.2h  0.94% Sitcom
    1481.8h  0.93% Börsenmagazin
    1435.7h  0.90% Wetterbericht
    1289.7h  0.81% Wirtschaftsmagazin
    1245.7h  0.78% Wissensmagazin
    1210.7h  0.76% Musikmagazin
    1207.8h  0.76% Quiz
    1111.4h  0.70% Telenovela
    1101.1h  0.69% Dramaserie
    1101.0h  0.69% Gesundheitsmagazin
    1081.6h  0.68% Sportmagazin
