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

**96** channels, **226,419.2** hours playtime between **2023-01-17** and **2023-05-22**


### playtime per genre (top 30)

    15194.5h 6.71% Nachrichten
    10964.6h 4.84% Verkaufsshow
    9150.5h  4.04% Krimiserie
    7526.2h  3.32% Werbesendung
    7394.9h  3.27% Dokureihe
    6738.4h  2.98% Dokusoap
    6479.4h  2.86% Regionalmagazin
    5793.9h  2.56% Dokumentation
    5597.2h  2.47% *unknown*
    4214.9h  1.86% Zeichentrickserie
    4147.0h  1.83% Infomercial
    4088.8h  1.81% Animationsserie
    3765.5h  1.66% Comedyserie
    3111.3h  1.37% Morgenmagazin
    3058.8h  1.35% Programmende
    2994.6h  1.32% Talkshow
    2970.9h  1.31% Religionsmagazin
    2600.6h  1.15% Magazin
    2261.1h  1.00% E-Sport
    2131.9h  0.94% Sitcom
    2052.7h  0.91% Börsenmagazin
    2050.2h  0.91% Wetterbericht
    1779.6h  0.79% Wirtschaftsmagazin
    1759.3h  0.78% Musikmagazin
    1759.2h  0.78% Wissensmagazin
    1732.8h  0.77% Quiz
    1594.3h  0.70% Komödie
    1581.7h  0.70% Sportmagazin
    1580.2h  0.70% Telenovela
    1521.9h  0.67% Gesundheitsmagazin
