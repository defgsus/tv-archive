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

**96** channels, **140,947.0** hours playtime between **2023-01-17** and **2023-04-05**


### playtime per genre (top 30)

    9820.5h 6.97% Nachrichten
    7014.3h 4.98% Verkaufsshow
    5880.1h 4.17% Krimiserie
    4752.9h 3.37% Werbesendung
    4467.1h 3.17% Dokureihe
    4315.5h 3.06% Dokusoap
    4142.0h 2.94% Regionalmagazin
    3501.6h 2.48% Dokumentation
    3260.8h 2.31% *unknown*
    2658.4h 1.89% Animationsserie
    2600.4h 1.84% Infomercial
    2585.3h 1.83% Zeichentrickserie
    2315.7h 1.64% Comedyserie
    2008.2h 1.42% Morgenmagazin
    1944.2h 1.38% Programmende
    1867.0h 1.32% Talkshow
    1839.2h 1.30% Religionsmagazin
    1501.3h 1.07% Magazin
    1449.9h 1.03% E-Sport
    1346.3h 0.96% Sitcom
    1332.0h 0.95% Börsenmagazin
    1262.2h 0.90% Wetterbericht
    1151.3h 0.82% Wirtschaftsmagazin
    1106.7h 0.79% Wissensmagazin
    1073.7h 0.76% Quiz
    1068.6h 0.76% Musikmagazin
    997.5h  0.71% Dramaserie
    992.9h  0.70% Telenovela
    974.1h  0.69% Sportmagazin
    969.4h  0.69% Gesundheitsmagazin
