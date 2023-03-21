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

**96** channels, **117,348.3** hours playtime between **2023-01-17** and **2023-03-22**


### playtime per genre (top 30)

    8240.4h 7.02% Nachrichten
    5881.2h 5.01% Verkaufsshow
    4904.9h 4.18% Krimiserie
    3965.0h 3.38% Werbesendung
    3712.7h 3.16% Dokusoap
    3609.3h 3.08% Dokureihe
    3455.0h 2.94% Regionalmagazin
    2871.6h 2.45% Dokumentation
    2743.5h 2.34% *unknown*
    2235.9h 1.91% Animationsserie
    2155.2h 1.84% Infomercial
    2128.2h 1.81% Zeichentrickserie
    1917.3h 1.63% Comedyserie
    1672.2h 1.43% Morgenmagazin
    1598.4h 1.36% Programmende
    1556.0h 1.33% Talkshow
    1526.3h 1.30% Religionsmagazin
    1224.3h 1.04% Magazin
    1218.0h 1.04% E-Sport
    1115.5h 0.95% Sitcom
    1100.6h 0.94% Börsenmagazin
    1045.7h 0.89% Wetterbericht
    958.2h  0.82% Wirtschaftsmagazin
    919.4h  0.78% Wissensmagazin
    883.8h  0.75% Quiz
    880.0h  0.75% Musikmagazin
    852.1h  0.73% Dramaserie
    817.9h  0.70% Telenovela
    810.2h  0.69% Gesundheitsmagazin
    798.7h  0.68% Sportmagazin
