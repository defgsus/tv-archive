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

**96** channels, **177,568.0** hours playtime between **2023-01-17** and **2023-04-25**


### playtime per genre (top 30)

    12084.4h 6.81% Nachrichten
    8750.1h  4.93% Verkaufsshow
    7270.9h  4.09% Krimiserie
    5933.8h  3.34% Werbesendung
    5733.4h  3.23% Dokureihe
    5281.0h  2.97% Dokusoap
    5119.6h  2.88% Regionalmagazin
    4466.2h  2.52% Dokumentation
    4265.0h  2.40% *unknown*
    3273.3h  1.84% Zeichentrickserie
    3261.2h  1.84% Animationsserie
    3246.8h  1.83% Infomercial
    2938.9h  1.66% Comedyserie
    2455.8h  1.38% Morgenmagazin
    2452.5h  1.38% Programmende
    2323.0h  1.31% Talkshow
    2316.5h  1.30% Religionsmagazin
    1940.7h  1.09% Magazin
    1812.1h  1.02% E-Sport
    1672.2h  0.94% Sitcom
    1618.1h  0.91% Börsenmagazin
    1603.4h  0.90% Wetterbericht
    1415.0h  0.80% Wirtschaftsmagazin
    1391.4h  0.78% Wissensmagazin
    1358.8h  0.77% Quiz
    1358.3h  0.76% Musikmagazin
    1236.1h  0.70% Telenovela
    1230.8h  0.69% Sportmagazin
    1224.7h  0.69% Gesundheitsmagazin
    1203.9h  0.68% Dramaserie
