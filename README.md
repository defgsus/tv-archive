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

**97** channels, **509,348.2** hours playtime between **2023-01-17** and **2023-10-27**


### playtime per genre (top 30)

    33578.6h 6.59% Nachrichten
    24323.5h 4.78% Verkaufsshow
    20490.3h 4.02% Krimiserie
    17222.8h 3.38% Werbesendung
    16764.8h 3.29% Dokureihe
    15532.7h 3.05% Dokusoap
    14721.7h 2.89% Regionalmagazin
    12932.1h 2.54% Dokumentation
    12240.1h 2.40% *unknown*
    9514.5h  1.87% Zeichentrickserie
    9277.4h  1.82% Infomercial
    9104.3h  1.79% Animationsserie
    8075.6h  1.59% Comedyserie
    7233.3h  1.42% Morgenmagazin
    6849.0h  1.34% Religionsmagazin
    6771.2h  1.33% Talkshow
    6414.1h  1.26% Magazin
    5236.7h  1.03% Programmende
    4996.8h  0.98% E-Sport
    4867.3h  0.96% Sitcom
    4735.9h  0.93% Wetterbericht
    4594.5h  0.90% Börsenmagazin
    4272.2h  0.84% Quiz
    3959.7h  0.78% Komödie
    3854.5h  0.76% Wissensmagazin
    3843.5h  0.75% Wirtschaftsmagazin
    3828.6h  0.75% Musikmagazin
    3661.7h  0.72% Telenovela
    3517.2h  0.69% Politikmagazin
    3371.2h  0.66% Realityshow
