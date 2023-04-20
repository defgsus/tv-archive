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

**96** channels, **170,275.4** hours playtime between **2023-01-17** and **2023-04-21**


### playtime per genre (top 30)

    11662.0h 6.85% Nachrichten
    8414.2h  4.94% Verkaufsshow
    6999.0h  4.11% Krimiserie
    5682.5h  3.34% Werbesendung
    5475.7h  3.22% Dokureihe
    5097.1h  2.99% Dokusoap
    4954.0h  2.91% Regionalmagazin
    4299.8h  2.53% Dokumentation
    4069.3h  2.39% *unknown*
    3142.5h  1.85% Animationsserie
    3129.1h  1.84% Zeichentrickserie
    3109.3h  1.83% Infomercial
    2816.3h  1.65% Comedyserie
    2376.6h  1.40% Morgenmagazin
    2359.1h  1.39% Programmende
    2209.9h  1.30% Religionsmagazin
    2205.1h  1.30% Talkshow
    1856.1h  1.09% Magazin
    1737.8h  1.02% E-Sport
    1608.0h  0.94% Sitcom
    1578.3h  0.93% Börsenmagazin
    1537.5h  0.90% Wetterbericht
    1369.8h  0.80% Wirtschaftsmagazin
    1336.2h  0.78% Wissensmagazin
    1299.6h  0.76% Musikmagazin
    1297.8h  0.76% Quiz
    1194.2h  0.70% Telenovela
    1178.3h  0.69% Gesundheitsmagazin
    1165.7h  0.68% Sportmagazin
    1164.4h  0.68% Dramaserie
