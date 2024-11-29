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

**109** channels, **1,159,909.5** hours playtime between **2023-01-17** and **2024-11-30**


### playtime per genre (top 30)

    75746.1h 6.53% Nachrichten
    52950.2h 4.57% Verkaufsshow
    48413.7h 4.17% Krimiserie
    42725.0h 3.68% Werbesendung
    36159.9h 3.12% Dokureihe
    34515.4h 2.98% Dokusoap
    33966.9h 2.93% Regionalmagazin
    30500.5h 2.63% Dokumentation
    27315.3h 2.35% *unknown*
    21730.9h 1.87% Zeichentrickserie
    21430.0h 1.85% Infomercial
    20731.8h 1.79% Animationsserie
    16564.5h 1.43% Comedyserie
    16249.5h 1.40% Morgenmagazin
    15426.4h 1.33% Religionsmagazin
    15392.0h 1.33% Talkshow
    14438.1h 1.24% Magazin
    11462.7h 0.99% E-Sport
    11201.4h 0.97% Sitcom
    10479.2h 0.90% Wetterbericht
    10263.9h 0.88% Quiz
    10244.9h 0.88% Programmende
    10168.4h 0.88% Komödie
    8920.0h  0.77% Realityshow
    8826.6h  0.76% Politikmagazin
    8711.4h  0.75% Wissensmagazin
    8613.7h  0.74% Börsenmagazin
    7765.4h  0.67% Wirtschaftsmagazin
    7688.6h  0.66% Telenovela
    7665.1h  0.66% Dramaserie
