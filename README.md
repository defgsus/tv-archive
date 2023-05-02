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

**96** channels, **192,131.8** hours playtime between **2023-01-17** and **2023-05-03**


### playtime per genre (top 30)

    13010.4h 6.77% Nachrichten
    9398.1h  4.89% Verkaufsshow
    7838.4h  4.08% Krimiserie
    6383.8h  3.32% Werbesendung
    6191.2h  3.22% Dokureihe
    5716.6h  2.98% Dokusoap
    5529.6h  2.88% Regionalmagazin
    4888.2h  2.54% Dokumentation
    4671.4h  2.43% *unknown*
    3557.5h  1.85% Zeichentrickserie
    3512.5h  1.83% Infomercial
    3502.2h  1.82% Animationsserie
    3188.6h  1.66% Comedyserie
    2653.1h  1.38% Morgenmagazin
    2641.4h  1.37% Programmende
    2516.6h  1.31% Talkshow
    2510.7h  1.31% Religionsmagazin
    2139.4h  1.11% Magazin
    1940.2h  1.01% E-Sport
    1816.0h  0.95% Sitcom
    1745.7h  0.91% Börsenmagazin
    1735.5h  0.90% Wetterbericht
    1522.5h  0.79% Wirtschaftsmagazin
    1502.3h  0.78% Wissensmagazin
    1479.8h  0.77% Musikmagazin
    1469.5h  0.76% Quiz
    1343.9h  0.70% Telenovela
    1336.8h  0.70% Sportmagazin
    1330.1h  0.69% Komödie
    1324.5h  0.69% Gesundheitsmagazin
