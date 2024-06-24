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

**109** channels, **917,950.3** hours playtime between **2023-01-17** and **2024-06-25**


### playtime per genre (top 30)

    59942.2h 6.53% Nachrichten
    43167.6h 4.70% Verkaufsshow
    37435.3h 4.08% Krimiserie
    32486.1h 3.54% Werbesendung
    28895.2h 3.15% Dokureihe
    27757.8h 3.02% Dokusoap
    26672.3h 2.91% Regionalmagazin
    23850.2h 2.60% Dokumentation
    23038.4h 2.51% *unknown*
    16891.8h 1.84% Zeichentrickserie
    16736.2h 1.82% Infomercial
    16394.0h 1.79% Animationsserie
    13721.5h 1.49% Comedyserie
    13096.1h 1.43% Magazin
    12919.9h 1.41% Morgenmagazin
    12441.0h 1.36% Religionsmagazin
    12216.2h 1.33% Talkshow
    9080.2h  0.99% E-Sport
    8588.0h  0.94% Sitcom
    8392.8h  0.91% Programmende
    8197.8h  0.89% Wetterbericht
    7945.0h  0.87% Komödie
    7934.9h  0.86% Quiz
    7835.8h  0.85% Börsenmagazin
    6894.4h  0.75% Politikmagazin
    6812.1h  0.74% Wissensmagazin
    6805.4h  0.74% Realityshow
    6431.8h  0.70% Wirtschaftsmagazin
    6310.9h  0.69% Telenovela
    6017.0h  0.66% Musikmagazin
