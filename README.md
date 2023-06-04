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

**96** channels, **251,531.1** hours playtime between **2023-01-17** and **2023-06-05**


### playtime per genre (top 30)

    16754.2h 6.66% Nachrichten
    12141.8h 4.83% Verkaufsshow
    10092.7h 4.01% Krimiserie
    8368.9h  3.33% Werbesendung
    8202.8h  3.26% Dokureihe
    7501.3h  2.98% Dokusoap
    7169.7h  2.85% Regionalmagazin
    6443.9h  2.56% Dokumentation
    6249.1h  2.48% *unknown*
    4734.4h  1.88% Zeichentrickserie
    4607.6h  1.83% Infomercial
    4490.2h  1.79% Animationsserie
    4172.8h  1.66% Comedyserie
    3457.9h  1.37% Morgenmagazin
    3327.9h  1.32% Talkshow
    3306.3h  1.31% Religionsmagazin
    3252.1h  1.29% Programmende
    2909.2h  1.16% Magazin
    2515.2h  1.00% E-Sport
    2353.6h  0.94% Sitcom
    2294.3h  0.91% Wetterbericht
    2265.9h  0.90% Börsenmagazin
    1970.4h  0.78% Wirtschaftsmagazin
    1957.6h  0.78% Musikmagazin
    1946.8h  0.77% Wissensmagazin
    1938.0h  0.77% Quiz
    1872.3h  0.74% Komödie
    1765.1h  0.70% Telenovela
    1729.5h  0.69% Sportmagazin
    1648.2h  0.66% Gesundheitsmagazin
