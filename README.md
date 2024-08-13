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

**109** channels, **996,028.4** hours playtime between **2023-01-17** and **2024-08-14**


### playtime per genre (top 30)

    64788.7h 6.50% Nachrichten
    46408.2h 4.66% Verkaufsshow
    40854.2h 4.10% Krimiserie
    35813.7h 3.60% Werbesendung
    31315.8h 3.14% Dokureihe
    30105.8h 3.02% Dokusoap
    29006.4h 2.91% Regionalmagazin
    25943.7h 2.60% Dokumentation
    24418.3h 2.45% *unknown*
    18462.1h 1.85% Zeichentrickserie
    18232.5h 1.83% Infomercial
    17817.6h 1.79% Animationsserie
    14677.0h 1.47% Comedyserie
    13964.8h 1.40% Morgenmagazin
    13547.6h 1.36% Religionsmagazin
    13485.2h 1.35% Magazin
    13075.0h 1.31% Talkshow
    9865.9h  0.99% E-Sport
    9467.1h  0.95% Sitcom
    8986.8h  0.90% Programmende
    8971.5h  0.90% Wetterbericht
    8721.2h  0.88% Komödie
    8571.6h  0.86% Quiz
    8092.4h  0.81% Börsenmagazin
    7457.8h  0.75% Politikmagazin
    7412.4h  0.74% Wissensmagazin
    7373.0h  0.74% Realityshow
    6822.8h  0.69% Wirtschaftsmagazin
    6556.5h  0.66% Telenovela
    6473.9h  0.65% Dramaserie
