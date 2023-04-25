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

**96** channels, **179,356.8** hours playtime between **2023-01-17** and **2023-04-26**


### playtime per genre (top 30)

    12213.5h 6.81% Nachrichten
    8837.3h  4.93% Verkaufsshow
    7359.3h  4.10% Krimiserie
    5988.2h  3.34% Werbesendung
    5782.2h  3.22% Dokureihe
    5331.0h  2.97% Dokusoap
    5170.7h  2.88% Regionalmagazin
    4506.9h  2.51% Dokumentation
    4321.3h  2.41% *unknown*
    3308.8h  1.84% Zeichentrickserie
    3292.6h  1.84% Animationsserie
    3281.0h  1.83% Infomercial
    2975.0h  1.66% Comedyserie
    2490.6h  1.39% Morgenmagazin
    2466.1h  1.37% Programmende
    2347.1h  1.31% Talkshow
    2337.1h  1.30% Religionsmagazin
    1963.5h  1.09% Magazin
    1829.2h  1.02% E-Sport
    1687.6h  0.94% Sitcom
    1634.6h  0.91% Börsenmagazin
    1620.7h  0.90% Wetterbericht
    1428.8h  0.80% Wirtschaftsmagazin
    1404.1h  0.78% Wissensmagazin
    1374.8h  0.77% Musikmagazin
    1372.9h  0.77% Quiz
    1257.0h  0.70% Telenovela
    1244.0h  0.69% Sportmagazin
    1239.2h  0.69% Gesundheitsmagazin
    1217.4h  0.68% Dramaserie
