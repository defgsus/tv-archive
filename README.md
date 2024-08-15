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

**109** channels, **999,692.9** hours playtime between **2023-01-17** and **2024-08-16**


### playtime per genre (top 30)

    65063.7h 6.51% Nachrichten
    46567.1h 4.66% Verkaufsshow
    40995.8h 4.10% Krimiserie
    35955.2h 3.60% Werbesendung
    31427.9h 3.14% Dokureihe
    30209.2h 3.02% Dokusoap
    29136.1h 2.91% Regionalmagazin
    26052.9h 2.61% Dokumentation
    24471.4h 2.45% *unknown*
    18524.3h 1.85% Zeichentrickserie
    18302.8h 1.83% Infomercial
    17899.3h 1.79% Animationsserie
    14722.1h 1.47% Comedyserie
    14032.6h 1.40% Morgenmagazin
    13588.4h 1.36% Religionsmagazin
    13502.8h 1.35% Magazin
    13099.0h 1.31% Talkshow
    9887.4h  0.99% E-Sport
    9511.5h  0.95% Sitcom
    9014.0h  0.90% Programmende
    9013.0h  0.90% Wetterbericht
    8750.8h  0.88% Komödie
    8613.1h  0.86% Quiz
    8110.6h  0.81% Börsenmagazin
    7492.6h  0.75% Politikmagazin
    7442.2h  0.74% Wissensmagazin
    7422.8h  0.74% Realityshow
    6848.5h  0.69% Wirtschaftsmagazin
    6578.3h  0.66% Telenovela
    6519.4h  0.65% Dramaserie
