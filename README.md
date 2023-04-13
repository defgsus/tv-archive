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

**96** channels, **157,469.0** hours playtime between **2023-01-17** and **2023-04-14**


### playtime per genre (top 30)

    10828.2h 6.88% Nachrichten
    7799.2h  4.95% Verkaufsshow
    6478.8h  4.11% Krimiserie
    5269.2h  3.35% Werbesendung
    5070.0h  3.22% Dokureihe
    4765.4h  3.03% Dokusoap
    4585.5h  2.91% Regionalmagazin
    3969.5h  2.52% Dokumentation
    3707.3h  2.35% *unknown*
    2925.1h  1.86% Animationsserie
    2885.1h  1.83% Zeichentrickserie
    2865.6h  1.82% Infomercial
    2590.3h  1.64% Comedyserie
    2200.0h  1.40% Morgenmagazin
    2185.2h  1.39% Programmende
    2049.4h  1.30% Religionsmagazin
    2018.9h  1.28% Talkshow
    1687.9h  1.07% Magazin
    1619.1h  1.03% E-Sport
    1487.0h  0.94% Sitcom
    1454.3h  0.92% Börsenmagazin
    1419.0h  0.90% Wetterbericht
    1273.4h  0.81% Wirtschaftsmagazin
    1232.3h  0.78% Wissensmagazin
    1193.5h  0.76% Musikmagazin
    1189.0h  0.76% Quiz
    1094.2h  0.69% Telenovela
    1090.4h  0.69% Gesundheitsmagazin
    1086.3h  0.69% Dramaserie
    1071.5h  0.68% Sportmagazin
