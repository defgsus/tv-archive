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

**109** channels, **984,945.6** hours playtime between **2023-01-17** and **2024-08-07**


### playtime per genre (top 30)

    64076.7h 6.51% Nachrichten
    45931.2h 4.66% Verkaufsshow
    40392.8h 4.10% Krimiserie
    35358.4h 3.59% Werbesendung
    30974.2h 3.14% Dokureihe
    29795.3h 3.03% Dokusoap
    28669.6h 2.91% Regionalmagazin
    25634.3h 2.60% Dokumentation
    24236.4h 2.46% *unknown*
    18259.0h 1.85% Zeichentrickserie
    18021.2h 1.83% Infomercial
    17617.0h 1.79% Animationsserie
    14554.9h 1.48% Comedyserie
    13826.8h 1.40% Morgenmagazin
    13454.4h 1.37% Magazin
    13386.5h 1.36% Religionsmagazin
    12953.3h 1.32% Talkshow
    9753.1h  0.99% E-Sport
    9341.2h  0.95% Sitcom
    8897.4h  0.90% Programmende
    8859.9h  0.90% Wetterbericht
    8628.4h  0.88% Komödie
    8470.2h  0.86% Quiz
    8056.0h  0.82% Börsenmagazin
    7391.2h  0.75% Politikmagazin
    7327.1h  0.74% Wissensmagazin
    7289.5h  0.74% Realityshow
    6769.6h  0.69% Wirtschaftsmagazin
    6511.5h  0.66% Telenovela
    6401.1h  0.65% Dramaserie
