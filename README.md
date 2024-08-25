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

**109** channels, **1,014,351.8** hours playtime between **2023-01-17** and **2024-08-26**


### playtime per genre (top 30)

    65950.6h 6.50% Nachrichten
    47227.8h 4.66% Verkaufsshow
    41685.7h 4.11% Krimiserie
    36578.5h 3.61% Werbesendung
    31913.9h 3.15% Dokureihe
    30660.5h 3.02% Dokusoap
    29546.2h 2.91% Regionalmagazin
    26492.2h 2.61% Dokumentation
    24738.1h 2.44% *unknown*
    18819.4h 1.86% Zeichentrickserie
    18581.9h 1.83% Infomercial
    18169.3h 1.79% Animationsserie
    14883.0h 1.47% Comedyserie
    14202.1h 1.40% Morgenmagazin
    13796.6h 1.36% Religionsmagazin
    13546.0h 1.34% Magazin
    13320.0h 1.31% Talkshow
    10027.5h 0.99% E-Sport
    9662.6h  0.95% Sitcom
    9162.0h  0.90% Wetterbericht
    9124.3h  0.90% Programmende
    8937.9h  0.88% Komödie
    8734.4h  0.86% Quiz
    8145.9h  0.80% Börsenmagazin
    7570.4h  0.75% Wissensmagazin
    7568.5h  0.75% Politikmagazin
    7506.2h  0.74% Realityshow
    6911.4h  0.68% Wirtschaftsmagazin
    6657.3h  0.66% Telenovela
    6610.1h  0.65% Dramaserie
