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

**96** channels, **151,986.1** hours playtime between **2023-01-17** and **2023-04-11**


### playtime per genre (top 30)

    10429.9h 6.86% Nachrichten
    7528.3h  4.95% Verkaufsshow
    6238.5h  4.10% Krimiserie
    5092.0h  3.35% Werbesendung
    4867.4h  3.20% Dokureihe
    4602.3h  3.03% Dokusoap
    4387.3h  2.89% Regionalmagazin
    3858.5h  2.54% Dokumentation
    3564.8h  2.35% *unknown*
    2839.5h  1.87% Animationsserie
    2782.5h  1.83% Zeichentrickserie
    2760.7h  1.82% Infomercial
    2478.0h  1.63% Comedyserie
    2104.7h  1.38% Programmende
    2099.6h  1.38% Morgenmagazin
    1989.0h  1.31% Religionsmagazin
    1964.6h  1.29% Talkshow
    1622.7h  1.07% Magazin
    1565.8h  1.03% E-Sport
    1426.9h  0.94% Sitcom
    1388.6h  0.91% Börsenmagazin
    1366.4h  0.90% Wetterbericht
    1224.5h  0.81% Wirtschaftsmagazin
    1184.1h  0.78% Wissensmagazin
    1149.4h  0.76% Musikmagazin
    1149.3h  0.76% Quiz
    1054.8h  0.69% Dramaserie
    1048.1h  0.69% Gesundheitsmagazin
    1040.6h  0.68% Sportmagazin
    1037.2h  0.68% Telenovela
