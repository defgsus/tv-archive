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

**96** channels, **186,704.0** hours playtime between **2023-01-17** and **2023-04-30**


### playtime per genre (top 30)

    12692.6h 6.80% Nachrichten
    9202.6h  4.93% Verkaufsshow
    7664.1h  4.10% Krimiserie
    6215.2h  3.33% Werbesendung
    6003.4h  3.22% Dokureihe
    5530.5h  2.96% Dokusoap
    5398.6h  2.89% Regionalmagazin
    4684.5h  2.51% Dokumentation
    4501.4h  2.41% *unknown*
    3452.9h  1.85% Zeichentrickserie
    3424.6h  1.83% Infomercial
    3411.7h  1.83% Animationsserie
    3099.9h  1.66% Comedyserie
    2599.8h  1.39% Morgenmagazin
    2581.8h  1.38% Programmende
    2441.7h  1.31% Talkshow
    2425.1h  1.30% Religionsmagazin
    2067.8h  1.11% Magazin
    1887.2h  1.01% E-Sport
    1766.1h  0.95% Sitcom
    1692.5h  0.91% Börsenmagazin
    1687.7h  0.90% Wetterbericht
    1484.2h  0.79% Wirtschaftsmagazin
    1465.0h  0.78% Wissensmagazin
    1437.2h  0.77% Quiz
    1427.1h  0.76% Musikmagazin
    1318.3h  0.71% Telenovela
    1296.5h  0.69% Gesundheitsmagazin
    1288.2h  0.69% Sportmagazin
    1267.8h  0.68% Dramaserie
