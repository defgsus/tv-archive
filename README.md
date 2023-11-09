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

**97** channels, **534,484.1** hours playtime between **2023-01-17** and **2023-11-10**


### playtime per genre (top 30)

    35208.9h 6.59% Nachrichten
    25542.5h 4.78% Verkaufsshow
    21514.3h 4.03% Krimiserie
    18113.1h 3.39% Werbesendung
    17487.8h 3.27% Dokureihe
    16256.0h 3.04% Dokusoap
    15453.3h 2.89% Regionalmagazin
    13626.0h 2.55% Dokumentation
    12952.5h 2.42% *unknown*
    9929.9h  1.86% Zeichentrickserie
    9730.5h  1.82% Infomercial
    9556.1h  1.79% Animationsserie
    8418.2h  1.58% Comedyserie
    7613.9h  1.42% Morgenmagazin
    7202.6h  1.35% Religionsmagazin
    7125.9h  1.33% Talkshow
    6780.5h  1.27% Magazin
    5428.8h  1.02% Programmende
    5249.6h  0.98% E-Sport
    5120.6h  0.96% Sitcom
    4940.2h  0.92% Wetterbericht
    4834.4h  0.90% Börsenmagazin
    4466.0h  0.84% Quiz
    4173.1h  0.78% Komödie
    4043.4h  0.76% Wissensmagazin
    4029.6h  0.75% Wirtschaftsmagazin
    3967.5h  0.74% Musikmagazin
    3859.0h  0.72% Telenovela
    3703.2h  0.69% Politikmagazin
    3642.2h  0.68% Realityshow
