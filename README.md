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

**108** channels, **876,211.8** hours playtime between **2023-01-17** and **2024-05-29**


### playtime per genre (top 30)

    57247.7h 6.53% Nachrichten
    41582.6h 4.75% Verkaufsshow
    35669.8h 4.07% Krimiserie
    30741.9h 3.51% Werbesendung
    27600.8h 3.15% Dokureihe
    26475.5h 3.02% Dokusoap
    25466.8h 2.91% Regionalmagazin
    22741.4h 2.60% Dokumentation
    22194.8h 2.53% *unknown*
    16104.8h 1.84% Zeichentrickserie
    15936.4h 1.82% Infomercial
    15611.5h 1.78% Animationsserie
    13159.3h 1.50% Comedyserie
    12447.5h 1.42% Magazin
    12329.4h 1.41% Morgenmagazin
    11855.5h 1.35% Religionsmagazin
    11667.0h 1.33% Talkshow
    8684.0h  0.99% E-Sport
    8101.2h  0.92% Sitcom
    8076.3h  0.92% Programmende
    7795.4h  0.89% Wetterbericht
    7676.6h  0.88% Börsenmagazin
    7581.4h  0.87% Quiz
    7564.5h  0.86% Komödie
    6477.3h  0.74% Wissensmagazin
    6466.9h  0.74% Realityshow
    6450.0h  0.74% Politikmagazin
    6211.5h  0.71% Wirtschaftsmagazin
    6168.2h  0.70% Telenovela
    5796.7h  0.66% Musikmagazin
