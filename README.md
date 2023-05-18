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

**96** channels, **221,017.0** hours playtime between **2023-01-17** and **2023-05-19**


### playtime per genre (top 30)

    14896.5h 6.74% Nachrichten
    10714.6h 4.85% Verkaufsshow
    8948.2h  4.05% Krimiserie
    7332.5h  3.32% Werbesendung
    7185.6h  3.25% Dokureihe
    6578.1h  2.98% Dokusoap
    6363.8h  2.88% Regionalmagazin
    5638.6h  2.55% Dokumentation
    5454.5h  2.47% *unknown*
    4113.1h  1.86% Zeichentrickserie
    4044.9h  1.83% Infomercial
    3983.9h  1.80% Animationsserie
    3698.4h  1.67% Comedyserie
    3062.4h  1.39% Morgenmagazin
    3017.4h  1.37% Programmende
    2905.8h  1.31% Talkshow
    2890.7h  1.31% Religionsmagazin
    2545.3h  1.15% Magazin
    2210.4h  1.00% E-Sport
    2088.6h  0.95% Sitcom
    2008.0h  0.91% Börsenmagazin
    2001.9h  0.91% Wetterbericht
    1751.2h  0.79% Wirtschaftsmagazin
    1724.0h  0.78% Wissensmagazin
    1706.5h  0.77% Musikmagazin
    1702.4h  0.77% Quiz
    1561.8h  0.71% Telenovela
    1537.2h  0.70% Komödie
    1533.9h  0.69% Sportmagazin
    1496.6h  0.68% Gesundheitsmagazin
