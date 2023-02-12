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

**96** channels, **50,148.6** hours playtime between **2023-01-17** and **2023-02-13**


### playtime per genre (top 30)

    3451.4h 6.88% Nachrichten
    2599.8h 5.18% Verkaufsshow
    2096.0h 4.18% Krimiserie
    1756.2h 3.50% Dokusoap
    1695.3h 3.38% Werbesendung
    1524.5h 3.04% Dokureihe
    1423.8h 2.84% Regionalmagazin
    1281.4h 2.56% Dokumentation
    1271.9h 2.54% *unknown*
    960.1h  1.91% Zeichentrickserie
    930.1h  1.85% Infomercial
    906.0h  1.81% Animationsserie
    824.6h  1.64% Comedyserie
    687.9h  1.37% Morgenmagazin
    670.0h  1.34% Programmende
    664.6h  1.33% Religionsmagazin
    656.9h  1.31% Talkshow
    568.2h  1.13% Magazin
    521.3h  1.04% E-Sport
    459.9h  0.92% Sitcom
    432.7h  0.86% Wetterbericht
    424.4h  0.85% Börsenmagazin
    413.9h  0.83% Wirtschaftsmagazin
    394.5h  0.79% Wissensmagazin
    379.5h  0.76% Quiz
    376.4h  0.75% Musikmagazin
    365.1h  0.73% Dramaserie
    354.0h  0.71% Gesundheitsmagazin
    344.3h  0.69% Telenovela
    336.1h  0.67% Wirtschaftstalk
