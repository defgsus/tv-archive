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

**109** channels, **990,532.6** hours playtime between **2023-01-17** and **2024-08-11**


### playtime per genre (top 30)

    64424.5h 6.50% Nachrichten
    46179.0h 4.66% Verkaufsshow
    40587.3h 4.10% Krimiserie
    35586.2h 3.59% Werbesendung
    31125.8h 3.14% Dokureihe
    29953.6h 3.02% Dokusoap
    28832.7h 2.91% Regionalmagazin
    25795.8h 2.60% Dokumentation
    24332.8h 2.46% *unknown*
    18364.7h 1.85% Zeichentrickserie
    18130.7h 1.83% Infomercial
    17712.8h 1.79% Animationsserie
    14609.9h 1.47% Comedyserie
    13894.9h 1.40% Morgenmagazin
    13464.1h 1.36% Magazin
    13456.5h 1.36% Religionsmagazin
    13014.8h 1.31% Talkshow
    9797.5h  0.99% E-Sport
    9406.5h  0.95% Sitcom
    8938.1h  0.90% Programmende
    8914.8h  0.90% Wetterbericht
    8675.2h  0.88% Komödie
    8517.5h  0.86% Quiz
    8074.5h  0.82% Börsenmagazin
    7417.3h  0.75% Politikmagazin
    7365.3h  0.74% Wissensmagazin
    7323.5h  0.74% Realityshow
    6797.1h  0.69% Wirtschaftsmagazin
    6535.6h  0.66% Telenovela
    6442.7h  0.65% Dramaserie
