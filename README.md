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

**96** channels, **172,090.2** hours playtime between **2023-01-17** and **2023-04-22**


### playtime per genre (top 30)

    11793.0h 6.85% Nachrichten
    8501.9h  4.94% Verkaufsshow
    7066.3h  4.11% Krimiserie
    5745.6h  3.34% Werbesendung
    5547.1h  3.22% Dokureihe
    5142.3h  2.99% Dokusoap
    5018.6h  2.92% Regionalmagazin
    4318.2h  2.51% Dokumentation
    4121.2h  2.39% *unknown*
    3171.0h  1.84% Animationsserie
    3163.9h  1.84% Zeichentrickserie
    3143.7h  1.83% Infomercial
    2847.2h  1.65% Comedyserie
    2408.9h  1.40% Morgenmagazin
    2372.9h  1.38% Programmende
    2240.0h  1.30% Talkshow
    2234.3h  1.30% Religionsmagazin
    1877.4h  1.09% Magazin
    1752.8h  1.02% E-Sport
    1625.4h  0.94% Sitcom
    1589.3h  0.92% Börsenmagazin
    1555.3h  0.90% Wetterbericht
    1385.8h  0.81% Wirtschaftsmagazin
    1352.5h  0.79% Wissensmagazin
    1315.4h  0.76% Quiz
    1313.6h  0.76% Musikmagazin
    1213.0h  0.70% Telenovela
    1189.6h  0.69% Gesundheitsmagazin
    1177.1h  0.68% Dramaserie
    1175.7h  0.68% Sportmagazin
