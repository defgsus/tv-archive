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

**108** channels, **885,401.2** hours playtime between **2023-01-17** and **2024-06-04**


### playtime per genre (top 30)

    57838.2h 6.53% Nachrichten
    41922.9h 4.73% Verkaufsshow
    36016.8h 4.07% Krimiserie
    31125.7h 3.52% Werbesendung
    27891.1h 3.15% Dokureihe
    26767.7h 3.02% Dokusoap
    25718.8h 2.90% Regionalmagazin
    22993.3h 2.60% Dokumentation
    22411.5h 2.53% *unknown*
    16279.3h 1.84% Zeichentrickserie
    16113.0h 1.82% Infomercial
    15778.2h 1.78% Animationsserie
    13284.0h 1.50% Comedyserie
    12605.6h 1.42% Magazin
    12452.5h 1.41% Morgenmagazin
    11984.7h 1.35% Religionsmagazin
    11790.9h 1.33% Talkshow
    8776.0h  0.99% E-Sport
    8213.0h  0.93% Sitcom
    8144.7h  0.92% Programmende
    7884.1h  0.89% Wetterbericht
    7733.1h  0.87% Börsenmagazin
    7666.8h  0.87% Quiz
    7659.3h  0.87% Komödie
    6558.6h  0.74% Wissensmagazin
    6547.6h  0.74% Realityshow
    6534.9h  0.74% Politikmagazin
    6263.4h  0.71% Wirtschaftsmagazin
    6202.4h  0.70% Telenovela
    5845.9h  0.66% Musikmagazin
