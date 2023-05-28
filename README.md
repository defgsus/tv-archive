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

**96** channels, **238,962.3** hours playtime between **2023-01-17** and **2023-05-29**


### playtime per genre (top 30)

    15985.9h 6.69% Nachrichten
    11558.0h 4.84% Verkaufsshow
    9619.2h  4.03% Krimiserie
    7953.4h  3.33% Werbesendung
    7791.3h  3.26% Dokureihe
    7099.9h  2.97% Dokusoap
    6835.0h  2.86% Regionalmagazin
    6096.8h  2.55% Dokumentation
    5918.3h  2.48% *unknown*
    4480.2h  1.87% Zeichentrickserie
    4383.9h  1.83% Infomercial
    4284.6h  1.79% Animationsserie
    3975.0h  1.66% Comedyserie
    3297.1h  1.38% Morgenmagazin
    3154.8h  1.32% Programmende
    3147.9h  1.32% Talkshow
    3140.6h  1.31% Religionsmagazin
    2748.8h  1.15% Magazin
    2390.2h  1.00% E-Sport
    2249.0h  0.94% Sitcom
    2186.3h  0.91% Börsenmagazin
    2171.1h  0.91% Wetterbericht
    1875.5h  0.78% Wirtschaftsmagazin
    1853.2h  0.78% Wissensmagazin
    1853.1h  0.78% Musikmagazin
    1843.0h  0.77% Quiz
    1713.9h  0.72% Komödie
    1679.2h  0.70% Telenovela
    1662.3h  0.70% Sportmagazin
    1592.1h  0.67% Gesundheitsmagazin
