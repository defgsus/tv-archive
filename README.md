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

**96** channels, **190,328.0** hours playtime between **2023-01-17** and **2023-05-02**


### playtime per genre (top 30)

    12877.8h 6.77% Nachrichten
    9331.4h  4.90% Verkaufsshow
    7753.4h  4.07% Krimiserie
    6329.7h  3.33% Werbesendung
    6137.8h  3.22% Dokureihe
    5670.1h  2.98% Dokusoap
    5464.9h  2.87% Regionalmagazin
    4821.6h  2.53% Dokumentation
    4609.1h  2.42% *unknown*
    3520.7h  1.85% Zeichentrickserie
    3478.7h  1.83% Infomercial
    3471.5h  1.82% Animationsserie
    3151.3h  1.66% Comedyserie
    2627.1h  1.38% Programmende
    2618.3h  1.38% Morgenmagazin
    2492.6h  1.31% Talkshow
    2486.4h  1.31% Religionsmagazin
    2116.0h  1.11% Magazin
    1916.4h  1.01% E-Sport
    1798.1h  0.94% Sitcom
    1718.0h  0.90% Wetterbericht
    1717.5h  0.90% Börsenmagazin
    1507.6h  0.79% Wirtschaftsmagazin
    1489.6h  0.78% Wissensmagazin
    1462.9h  0.77% Musikmagazin
    1456.3h  0.77% Quiz
    1325.4h  0.70% Telenovela
    1322.7h  0.69% Sportmagazin
    1317.7h  0.69% Komödie
    1313.3h  0.69% Gesundheitsmagazin
