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

**96** channels, **79,275.9** hours playtime between **2023-01-17** and **2023-03-01**


### playtime per genre (top 30)

    5619.1h 7.09% Nachrichten
    3999.1h 5.04% Verkaufsshow
    3360.4h 4.24% Krimiserie
    2692.2h 3.40% Werbesendung
    2612.3h 3.30% Dokusoap
    2360.2h 2.98% Dokureihe
    2326.3h 2.93% Regionalmagazin
    1945.5h 2.45% Dokumentation
    1897.7h 2.39% *unknown*
    1501.0h 1.89% Animationsserie
    1459.4h 1.84% Zeichentrickserie
    1450.5h 1.83% Infomercial
    1287.5h 1.62% Comedyserie
    1128.6h 1.42% Morgenmagazin
    1060.5h 1.34% Programmende
    1043.0h 1.32% Religionsmagazin
    1037.8h 1.31% Talkshow
    850.8h  1.07% Magazin
    820.2h  1.03% E-Sport
    742.7h  0.94% Sitcom
    717.0h  0.90% Börsenmagazin
    698.6h  0.88% Wetterbericht
    641.0h  0.81% Wirtschaftsmagazin
    621.5h  0.78% Wissensmagazin
    597.8h  0.75% Quiz
    582.6h  0.73% Musikmagazin
    575.2h  0.73% Dramaserie
    564.7h  0.71% Gesundheitsmagazin
    543.9h  0.69% Telenovela
    511.7h  0.65% Sportmagazin
