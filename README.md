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

**96** channels, **139,152.6** hours playtime between **2023-01-17** and **2023-04-04**


### playtime per genre (top 30)

    9697.5h 6.97% Nachrichten
    6929.9h 4.98% Verkaufsshow
    5785.5h 4.16% Krimiserie
    4696.9h 3.38% Werbesendung
    4386.9h 3.15% Dokureihe
    4259.2h 3.06% Dokusoap
    4080.0h 2.93% Regionalmagazin
    3457.6h 2.48% Dokumentation
    3197.2h 2.30% *unknown*
    2626.6h 1.89% Animationsserie
    2565.6h 1.84% Infomercial
    2548.2h 1.83% Zeichentrickserie
    2285.1h 1.64% Comedyserie
    1975.4h 1.42% Morgenmagazin
    1930.6h 1.39% Programmende
    1849.3h 1.33% Talkshow
    1816.5h 1.31% Religionsmagazin
    1475.1h 1.06% Magazin
    1438.7h 1.03% E-Sport
    1327.2h 0.95% Sitcom
    1315.0h 0.94% Börsenmagazin
    1244.7h 0.89% Wetterbericht
    1136.4h 0.82% Wirtschaftsmagazin
    1093.8h 0.79% Wissensmagazin
    1064.5h 0.76% Quiz
    1052.8h 0.76% Musikmagazin
    988.2h  0.71% Dramaserie
    972.8h  0.70% Telenovela
    963.3h  0.69% Sportmagazin
    954.6h  0.69% Gesundheitsmagazin
