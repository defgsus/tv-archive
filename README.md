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

**97** channels, **507,560.5** hours playtime between **2023-01-17** and **2023-10-26**


### playtime per genre (top 30)

    33452.4h 6.59% Nachrichten
    24245.0h 4.78% Verkaufsshow
    20406.5h 4.02% Krimiserie
    17163.9h 3.38% Werbesendung
    16710.3h 3.29% Dokureihe
    15475.5h 3.05% Dokusoap
    14662.1h 2.89% Regionalmagazin
    12870.9h 2.54% Dokumentation
    12196.8h 2.40% *unknown*
    9485.7h  1.87% Zeichentrickserie
    9244.7h  1.82% Infomercial
    9067.5h  1.79% Animationsserie
    8054.9h  1.59% Comedyserie
    7197.5h  1.42% Morgenmagazin
    6828.6h  1.35% Religionsmagazin
    6759.9h  1.33% Talkshow
    6384.6h  1.26% Magazin
    5222.8h  1.03% Programmende
    4989.5h  0.98% E-Sport
    4848.6h  0.96% Sitcom
    4717.6h  0.93% Wetterbericht
    4584.1h  0.90% Börsenmagazin
    4260.5h  0.84% Quiz
    3931.2h  0.77% Komödie
    3841.8h  0.76% Wissensmagazin
    3827.9h  0.75% Wirtschaftsmagazin
    3817.4h  0.75% Musikmagazin
    3642.3h  0.72% Telenovela
    3498.1h  0.69% Politikmagazin
    3345.8h  0.66% Realityshow
