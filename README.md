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

**96** channels, **57,422.3** hours playtime between **2023-01-17** and **2023-02-17**


### playtime per genre (top 30)

    4030.8h 7.02% Nachrichten
    2957.9h 5.15% Verkaufsshow
    2449.3h 4.27% Krimiserie
    1991.7h 3.47% Dokusoap
    1935.8h 3.37% Werbesendung
    1688.3h 2.94% Dokureihe
    1673.2h 2.91% Regionalmagazin
    1438.4h 2.51% Dokumentation
    1432.4h 2.49% *unknown*
    1089.8h 1.90% Zeichentrickserie
    1059.2h 1.84% Infomercial
    1054.6h 1.84% Animationsserie
    963.1h  1.68% Comedyserie
    824.5h  1.44% Morgenmagazin
    767.5h  1.34% Programmende
    752.9h  1.31% Talkshow
    747.4h  1.30% Religionsmagazin
    627.7h  1.09% Magazin
    604.3h  1.05% E-Sport
    540.8h  0.94% Sitcom
    503.0h  0.88% Börsenmagazin
    501.7h  0.87% Wetterbericht
    481.4h  0.84% Wirtschaftsmagazin
    447.6h  0.78% Wissensmagazin
    441.5h  0.77% Quiz
    424.4h  0.74% Dramaserie
    423.8h  0.74% Musikmagazin
    410.1h  0.71% Telenovela
    409.3h  0.71% Gesundheitsmagazin
    377.9h  0.66% Wirtschaftstalk
