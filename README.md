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

**96** channels, **146,476.7** hours playtime between **2023-01-17** and **2023-04-08**


### playtime per genre (top 30)

    10180.5h 6.95% Nachrichten
    7272.1h  4.96% Verkaufsshow
    6067.6h  4.14% Krimiserie
    4914.0h  3.35% Werbesendung
    4655.4h  3.18% Dokureihe
    4477.4h  3.06% Dokusoap
    4305.3h  2.94% Regionalmagazin
    3670.8h  2.51% Dokumentation
    3404.2h  2.32% *unknown*
    2752.9h  1.88% Animationsserie
    2694.3h  1.84% Infomercial
    2686.4h  1.83% Zeichentrickserie
    2410.3h  1.65% Comedyserie
    2084.4h  1.42% Morgenmagazin
    2024.9h  1.38% Programmende
    1915.7h  1.31% Talkshow
    1898.2h  1.30% Religionsmagazin
    1572.5h  1.07% Magazin
    1512.5h  1.03% E-Sport
    1400.9h  0.96% Sitcom
    1361.6h  0.93% Börsenmagazin
    1313.7h  0.90% Wetterbericht
    1196.1h  0.82% Wirtschaftsmagazin
    1148.6h  0.78% Wissensmagazin
    1114.9h  0.76% Quiz
    1105.1h  0.75% Musikmagazin
    1036.4h  0.71% Telenovela
    1024.6h  0.70% Dramaserie
    1011.5h  0.69% Gesundheitsmagazin
    998.5h   0.68% Sportmagazin
