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

**96** channels, **242,531.6** hours playtime between **2023-01-17** and **2023-05-31**


### playtime per genre (top 30)

    16200.8h 6.68% Nachrichten
    11722.8h 4.83% Verkaufsshow
    9752.0h  4.02% Krimiserie
    8059.5h  3.32% Werbesendung
    7903.9h  3.26% Dokureihe
    7231.2h  2.98% Dokusoap
    6924.0h  2.85% Regionalmagazin
    6235.9h  2.57% Dokumentation
    6015.8h  2.48% *unknown*
    4548.3h  1.88% Zeichentrickserie
    4438.5h  1.83% Infomercial
    4347.6h  1.79% Animationsserie
    4033.3h  1.66% Comedyserie
    3340.0h  1.38% Morgenmagazin
    3185.2h  1.31% Talkshow
    3182.7h  1.31% Programmende
    3180.3h  1.31% Religionsmagazin
    2782.7h  1.15% Magazin
    2418.7h  1.00% E-Sport
    2274.3h  0.94% Sitcom
    2219.5h  0.92% Börsenmagazin
    2205.9h  0.91% Wetterbericht
    1901.7h  0.78% Wirtschaftsmagazin
    1879.1h  0.77% Musikmagazin
    1875.5h  0.77% Wissensmagazin
    1872.3h  0.77% Quiz
    1766.4h  0.73% Komödie
    1701.2h  0.70% Telenovela
    1688.7h  0.70% Sportmagazin
    1607.2h  0.66% Gesundheitsmagazin
