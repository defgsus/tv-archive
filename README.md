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

**97** channels, **541,685.4** hours playtime between **2023-01-17** and **2023-11-14**


### playtime per genre (top 30)

    35633.8h 6.58% Nachrichten
    25871.4h 4.78% Verkaufsshow
    21797.2h 4.02% Krimiserie
    18368.1h 3.39% Werbesendung
    17712.6h 3.27% Dokureihe
    16433.5h 3.03% Dokusoap
    15630.4h 2.89% Regionalmagazin
    13812.7h 2.55% Dokumentation
    13162.2h 2.43% *unknown*
    10054.4h 1.86% Zeichentrickserie
    9870.4h  1.82% Infomercial
    9674.2h  1.79% Animationsserie
    8515.4h  1.57% Comedyserie
    7693.7h  1.42% Morgenmagazin
    7306.1h  1.35% Religionsmagazin
    7242.6h  1.34% Talkshow
    6884.8h  1.27% Magazin
    5485.3h  1.01% Programmende
    5307.4h  0.98% E-Sport
    5189.6h  0.96% Sitcom
    4987.2h  0.92% Wetterbericht
    4901.5h  0.90% Börsenmagazin
    4518.6h  0.83% Quiz
    4235.4h  0.78% Komödie
    4101.9h  0.76% Wissensmagazin
    4071.4h  0.75% Wirtschaftsmagazin
    4011.2h  0.74% Musikmagazin
    3897.2h  0.72% Telenovela
    3753.7h  0.69% Politikmagazin
    3698.7h  0.68% Realityshow
