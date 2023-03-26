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

**96** channels, **124,647.3** hours playtime between **2023-01-17** and **2023-03-27**


### playtime per genre (top 30)

    8692.1h 6.97% Nachrichten
    6243.2h 5.01% Verkaufsshow
    5187.9h 4.16% Krimiserie
    4213.0h 3.38% Werbesendung
    3886.9h 3.12% Dokusoap
    3877.2h 3.11% Dokureihe
    3641.8h 2.92% Regionalmagazin
    3085.8h 2.48% Dokumentation
    2888.7h 2.32% *unknown*
    2370.8h 1.90% Animationsserie
    2292.9h 1.84% Infomercial
    2267.3h 1.82% Zeichentrickserie
    2029.7h 1.63% Comedyserie
    1755.8h 1.41% Morgenmagazin
    1738.7h 1.39% Programmende
    1657.5h 1.33% Talkshow
    1629.2h 1.31% Religionsmagazin
    1298.5h 1.04% Magazin
    1285.1h 1.03% E-Sport
    1186.6h 0.95% Sitcom
    1152.5h 0.92% Börsenmagazin
    1111.6h 0.89% Wetterbericht
    1016.9h 0.82% Wirtschaftsmagazin
    974.2h  0.78% Wissensmagazin
    943.4h  0.76% Musikmagazin
    931.9h  0.75% Quiz
    903.3h  0.72% Dramaserie
    860.3h  0.69% Sportmagazin
    859.2h  0.69% Telenovela
    857.5h  0.69% Gesundheitsmagazin
