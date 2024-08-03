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

**109** channels, **979,570.6** hours playtime between **2023-01-17** and **2024-08-04**


### playtime per genre (top 30)

    63737.5h 6.51% Nachrichten
    45711.4h 4.67% Verkaufsshow
    40153.4h 4.10% Krimiserie
    35131.5h 3.59% Werbesendung
    30803.1h 3.14% Dokureihe
    29652.4h 3.03% Dokusoap
    28501.2h 2.91% Regionalmagazin
    25495.2h 2.60% Dokumentation
    24182.3h 2.47% *unknown*
    18154.0h 1.85% Zeichentrickserie
    17921.5h 1.83% Infomercial
    17520.5h 1.79% Animationsserie
    14493.6h 1.48% Comedyserie
    13762.3h 1.40% Morgenmagazin
    13448.4h 1.37% Magazin
    13302.4h 1.36% Religionsmagazin
    12902.5h 1.32% Talkshow
    9696.5h  0.99% E-Sport
    9282.1h  0.95% Sitcom
    8855.5h  0.90% Programmende
    8806.3h  0.90% Wetterbericht
    8575.8h  0.88% Komödie
    8430.9h  0.86% Quiz
    8038.2h  0.82% Börsenmagazin
    7354.5h  0.75% Politikmagazin
    7281.4h  0.74% Wissensmagazin
    7245.4h  0.74% Realityshow
    6742.6h  0.69% Wirtschaftsmagazin
    6495.1h  0.66% Telenovela
    6378.3h  0.65% Dramaserie
