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

**96** channels, **166,617.8** hours playtime between **2023-01-17** and **2023-04-19**


### playtime per genre (top 30)

    11383.4h 6.83% Nachrichten
    8242.1h  4.95% Verkaufsshow
    6848.2h  4.11% Krimiserie
    5570.7h  3.34% Werbesendung
    5391.8h  3.24% Dokureihe
    4987.6h  2.99% Dokusoap
    4828.2h  2.90% Regionalmagazin
    4212.3h  2.53% Dokumentation
    3973.9h  2.39% *unknown*
    3083.7h  1.85% Animationsserie
    3059.1h  1.84% Zeichentrickserie
    3037.1h  1.82% Infomercial
    2731.4h  1.64% Comedyserie
    2311.9h  1.39% Morgenmagazin
    2292.7h  1.38% Programmende
    2171.6h  1.30% Religionsmagazin
    2155.7h  1.29% Talkshow
    1804.4h  1.08% Magazin
    1711.4h  1.03% E-Sport
    1568.2h  0.94% Sitcom
    1554.7h  0.93% Börsenmagazin
    1502.9h  0.90% Wetterbericht
    1335.3h  0.80% Wirtschaftsmagazin
    1302.4h  0.78% Wissensmagazin
    1272.0h  0.76% Musikmagazin
    1260.2h  0.76% Quiz
    1154.8h  0.69% Telenovela
    1148.0h  0.69% Gesundheitsmagazin
    1146.8h  0.69% Sportmagazin
    1141.2h  0.68% Dramaserie
