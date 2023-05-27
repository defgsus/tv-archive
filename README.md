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

**96** channels, **237,166.7** hours playtime between **2023-01-17** and **2023-05-28**


### playtime per genre (top 30)

    15886.8h 6.70% Nachrichten
    11470.5h 4.84% Verkaufsshow
    9585.2h  4.04% Krimiserie
    7889.1h  3.33% Werbesendung
    7720.5h  3.26% Dokureihe
    7047.6h  2.97% Dokusoap
    6808.5h  2.87% Regionalmagazin
    6032.4h  2.54% Dokumentation
    5876.9h  2.48% *unknown*
    4443.2h  1.87% Zeichentrickserie
    4354.8h  1.84% Infomercial
    4256.4h  1.79% Animationsserie
    3962.7h  1.67% Comedyserie
    3291.1h  1.39% Morgenmagazin
    3141.1h  1.32% Programmende
    3119.2h  1.32% Talkshow
    3098.6h  1.31% Religionsmagazin
    2732.0h  1.15% Magazin
    2378.0h  1.00% E-Sport
    2241.9h  0.95% Sitcom
    2169.3h  0.91% Börsenmagazin
    2157.0h  0.91% Wetterbericht
    1866.1h  0.79% Wirtschaftsmagazin
    1842.2h  0.78% Wissensmagazin
    1835.9h  0.77% Musikmagazin
    1833.0h  0.77% Quiz
    1679.2h  0.71% Telenovela
    1678.6h  0.71% Komödie
    1648.0h  0.69% Sportmagazin
    1586.6h  0.67% Gesundheitsmagazin
