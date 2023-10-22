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

**97** channels, **502,206.9** hours playtime between **2023-01-17** and **2023-10-23**


### playtime per genre (top 30)

    33060.0h 6.58% Nachrichten
    23975.2h 4.77% Verkaufsshow
    20196.5h 4.02% Krimiserie
    16976.7h 3.38% Werbesendung
    16529.9h 3.29% Dokureihe
    15326.3h 3.05% Dokusoap
    14466.7h 2.88% Regionalmagazin
    12727.0h 2.53% Dokumentation
    12083.5h 2.41% *unknown*
    9392.2h  1.87% Zeichentrickserie
    9145.8h  1.82% Infomercial
    8963.7h  1.78% Animationsserie
    7970.4h  1.59% Comedyserie
    7091.3h  1.41% Morgenmagazin
    6759.3h  1.35% Religionsmagazin
    6696.4h  1.33% Talkshow
    6317.0h  1.26% Magazin
    5181.7h  1.03% Programmende
    4942.8h  0.98% E-Sport
    4782.2h  0.95% Sitcom
    4665.9h  0.93% Wetterbericht
    4527.7h  0.90% Börsenmagazin
    4206.4h  0.84% Quiz
    3915.4h  0.78% Komödie
    3793.8h  0.76% Wissensmagazin
    3789.8h  0.75% Musikmagazin
    3780.2h  0.75% Wirtschaftsmagazin
    3583.1h  0.71% Telenovela
    3439.0h  0.68% Politikmagazin
    3291.2h  0.66% Realityshow
