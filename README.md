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

**96** channels, **155,628.7** hours playtime between **2023-01-17** and **2023-04-13**


### playtime per genre (top 30)

    10695.2h 6.87% Nachrichten
    7713.2h  4.96% Verkaufsshow
    6405.3h  4.12% Krimiserie
    5208.9h  3.35% Werbesendung
    5003.5h  3.22% Dokureihe
    4703.0h  3.02% Dokusoap
    4516.0h  2.90% Regionalmagazin
    3931.8h  2.53% Dokumentation
    3666.4h  2.36% *unknown*
    2893.9h  1.86% Animationsserie
    2852.2h  1.83% Zeichentrickserie
    2829.7h  1.82% Infomercial
    2554.8h  1.64% Comedyserie
    2167.2h  1.39% Morgenmagazin
    2150.2h  1.38% Programmende
    2030.6h  1.30% Religionsmagazin
    1999.3h  1.28% Talkshow
    1659.4h  1.07% Magazin
    1602.2h  1.03% E-Sport
    1469.5h  0.94% Sitcom
    1443.0h  0.93% Börsenmagazin
    1401.2h  0.90% Wetterbericht
    1257.2h  0.81% Wirtschaftsmagazin
    1219.6h  0.78% Wissensmagazin
    1177.4h  0.76% Musikmagazin
    1176.8h  0.76% Quiz
    1079.9h  0.69% Gesundheitsmagazin
    1075.1h  0.69% Dramaserie
    1074.7h  0.69% Telenovela
    1063.4h  0.68% Sportmagazin
