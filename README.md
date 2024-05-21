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

**108** channels, **865,228.7** hours playtime between **2023-01-17** and **2024-05-22**


### playtime per genre (top 30)

    56484.8h 6.53% Nachrichten
    41149.8h 4.76% Verkaufsshow
    35218.8h 4.07% Krimiserie
    30311.2h 3.50% Werbesendung
    27258.1h 3.15% Dokureihe
    26153.4h 3.02% Dokusoap
    25142.8h 2.91% Regionalmagazin
    22453.5h 2.60% Dokumentation
    21962.7h 2.54% *unknown*
    15905.9h 1.84% Zeichentrickserie
    15728.0h 1.82% Infomercial
    15404.5h 1.78% Animationsserie
    13018.3h 1.50% Comedyserie
    12281.2h 1.42% Magazin
    12173.2h 1.41% Morgenmagazin
    11705.8h 1.35% Religionsmagazin
    11516.5h 1.33% Talkshow
    8575.4h  0.99% E-Sport
    7993.9h  0.92% Programmende
    7986.4h  0.92% Sitcom
    7692.8h  0.89% Wetterbericht
    7599.5h  0.88% Börsenmagazin
    7481.0h  0.86% Quiz
    7467.3h  0.86% Komödie
    6392.3h  0.74% Wissensmagazin
    6383.4h  0.74% Realityshow
    6350.6h  0.73% Politikmagazin
    6150.8h  0.71% Wirtschaftsmagazin
    6123.1h  0.71% Telenovela
    5727.8h  0.66% Musikmagazin
