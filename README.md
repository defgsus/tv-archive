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

**96** channels, **126,423.0** hours playtime between **2023-01-17** and **2023-03-28**


### playtime per genre (top 30)

    8840.0h 6.99% Nachrichten
    6329.4h 5.01% Verkaufsshow
    5252.7h 4.15% Krimiserie
    4272.3h 3.38% Werbesendung
    3945.5h 3.12% Dokureihe
    3937.0h 3.11% Dokusoap
    3704.7h 2.93% Regionalmagazin
    3124.8h 2.47% Dokumentation
    2919.0h 2.31% *unknown*
    2403.3h 1.90% Animationsserie
    2326.6h 1.84% Infomercial
    2303.6h 1.82% Zeichentrickserie
    2066.0h 1.63% Comedyserie
    1790.5h 1.42% Morgenmagazin
    1752.7h 1.39% Programmende
    1681.3h 1.33% Talkshow
    1642.9h 1.30% Religionsmagazin
    1322.0h 1.05% Magazin
    1302.2h 1.03% E-Sport
    1204.5h 0.95% Sitcom
    1178.7h 0.93% Börsenmagazin
    1131.9h 0.90% Wetterbericht
    1034.5h 0.82% Wirtschaftsmagazin
    987.5h  0.78% Wissensmagazin
    961.8h  0.76% Quiz
    954.6h  0.76% Musikmagazin
    916.4h  0.72% Dramaserie
    878.7h  0.70% Telenovela
    870.3h  0.69% Sportmagazin
    866.9h  0.69% Gesundheitsmagazin
