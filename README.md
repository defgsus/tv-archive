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

**97** channels, **498,607.8** hours playtime between **2023-01-17** and **2023-10-21**


### playtime per genre (top 30)

    32880.5h 6.59% Nachrichten
    23816.8h 4.78% Verkaufsshow
    20062.3h 4.02% Krimiserie
    16842.6h 3.38% Werbesendung
    16401.2h 3.29% Dokureihe
    15220.4h 3.05% Dokusoap
    14404.6h 2.89% Regionalmagazin
    12597.1h 2.53% Dokumentation
    11984.5h 2.40% *unknown*
    9327.4h  1.87% Zeichentrickserie
    9079.9h  1.82% Infomercial
    8898.9h  1.78% Animationsserie
    7940.7h  1.59% Comedyserie
    7075.4h  1.42% Morgenmagazin
    6693.7h  1.34% Religionsmagazin
    6642.6h  1.33% Talkshow
    6256.1h  1.25% Magazin
    5153.2h  1.03% Programmende
    4903.8h  0.98% E-Sport
    4757.5h  0.95% Sitcom
    4637.9h  0.93% Wetterbericht
    4502.8h  0.90% Börsenmagazin
    4195.5h  0.84% Quiz
    3850.2h  0.77% Komödie
    3769.6h  0.76% Wirtschaftsmagazin
    3767.3h  0.76% Musikmagazin
    3765.4h  0.76% Wissensmagazin
    3580.8h  0.72% Telenovela
    3428.0h  0.69% Politikmagazin
    3261.4h  0.65% Realityshow
