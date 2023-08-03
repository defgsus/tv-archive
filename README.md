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

**96** channels, **358,956.8** hours playtime between **2023-01-17** and **2023-08-04**


### playtime per genre (top 30)

    23820.2h 6.64% Nachrichten
    17112.2h 4.77% Verkaufsshow
    14491.6h 4.04% Krimiserie
    12068.1h 3.36% Werbesendung
    11754.5h 3.27% Dokureihe
    10854.0h 3.02% Dokusoap
    10313.6h 2.87% Regionalmagazin
    9064.5h  2.53% Dokumentation
    8726.0h  2.43% *unknown*
    6794.2h  1.89% Zeichentrickserie
    6565.3h  1.83% Infomercial
    6347.9h  1.77% Animationsserie
    5912.9h  1.65% Comedyserie
    5043.7h  1.41% Morgenmagazin
    4759.0h  1.33% Religionsmagazin
    4734.3h  1.32% Talkshow
    4286.1h  1.19% Magazin
    4071.6h  1.13% Programmende
    3556.2h  0.99% E-Sport
    3384.5h  0.94% Sitcom
    3371.6h  0.94% Wetterbericht
    3255.2h  0.91% Börsenmagazin
    2870.5h  0.80% Quiz
    2810.8h  0.78% Musikmagazin
    2765.5h  0.77% Wirtschaftsmagazin
    2745.1h  0.76% Komödie
    2712.3h  0.76% Wissensmagazin
    2491.2h  0.69% Telenovela
    2340.7h  0.65% Sportmagazin
    2310.6h  0.64% Reportagereihe
