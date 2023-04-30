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

**96** channels, **188,530.7** hours playtime between **2023-01-17** and **2023-05-01**


### playtime per genre (top 30)

    12774.2h 6.78% Nachrichten
    9274.9h  4.92% Verkaufsshow
    7730.0h  4.10% Krimiserie
    6274.9h  3.33% Werbesendung
    6095.7h  3.23% Dokureihe
    5578.3h  2.96% Dokusoap
    5430.6h  2.88% Regionalmagazin
    4735.4h  2.51% Dokumentation
    4538.4h  2.41% *unknown*
    3487.4h  1.85% Zeichentrickserie
    3457.5h  1.83% Infomercial
    3441.8h  1.83% Animationsserie
    3121.2h  1.66% Comedyserie
    2613.1h  1.39% Programmende
    2607.8h  1.38% Morgenmagazin
    2483.5h  1.32% Talkshow
    2466.2h  1.31% Religionsmagazin
    2100.9h  1.11% Magazin
    1905.7h  1.01% E-Sport
    1779.8h  0.94% Sitcom
    1709.5h  0.91% Börsenmagazin
    1701.6h  0.90% Wetterbericht
    1495.0h  0.79% Wirtschaftsmagazin
    1478.8h  0.78% Wissensmagazin
    1452.3h  0.77% Musikmagazin
    1441.0h  0.76% Quiz
    1318.3h  0.70% Telenovela
    1312.5h  0.70% Sportmagazin
    1304.5h  0.69% Gesundheitsmagazin
    1279.6h  0.68% Dramaserie
