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

**96** channels, **164,785.5** hours playtime between **2023-01-17** and **2023-04-18**


### playtime per genre (top 30)

    11253.4h 6.83% Nachrichten
    8147.9h  4.94% Verkaufsshow
    6761.0h  4.10% Krimiserie
    5514.6h  3.35% Werbesendung
    5325.5h  3.23% Dokureihe
    4937.9h  3.00% Dokusoap
    4763.8h  2.89% Regionalmagazin
    4164.9h  2.53% Dokumentation
    3907.2h  2.37% *unknown*
    3052.6h  1.85% Animationsserie
    3024.2h  1.84% Zeichentrickserie
    3001.6h  1.82% Infomercial
    2700.2h  1.64% Comedyserie
    2279.6h  1.38% Morgenmagazin
    2279.3h  1.38% Programmende
    2152.2h  1.31% Religionsmagazin
    2134.2h  1.30% Talkshow
    1785.0h  1.08% Magazin
    1695.5h  1.03% E-Sport
    1552.2h  0.94% Sitcom
    1526.2h  0.93% Börsenmagazin
    1486.5h  0.90% Wetterbericht
    1321.1h  0.80% Wirtschaftsmagazin
    1289.6h  0.78% Wissensmagazin
    1255.6h  0.76% Musikmagazin
    1249.6h  0.76% Quiz
    1135.4h  0.69% Sportmagazin
    1133.8h  0.69% Telenovela
    1132.3h  0.69% Gesundheitsmagazin
    1127.3h  0.68% Dramaserie
