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

**97** channels, **516,519.7** hours playtime between **2023-01-17** and **2023-10-31**


### playtime per genre (top 30)

    34007.9h 6.58% Nachrichten
    24656.8h 4.77% Verkaufsshow
    20759.3h 4.02% Krimiserie
    17495.8h 3.39% Werbesendung
    17002.0h 3.29% Dokureihe
    15732.1h 3.05% Dokusoap
    14899.2h 2.88% Regionalmagazin
    13142.3h 2.54% Dokumentation
    12444.4h 2.41% *unknown*
    9629.0h  1.86% Zeichentrickserie
    9409.4h  1.82% Infomercial
    9237.4h  1.79% Animationsserie
    8169.0h  1.58% Comedyserie
    7319.6h  1.42% Morgenmagazin
    6958.4h  1.35% Religionsmagazin
    6880.0h  1.33% Talkshow
    6505.0h  1.26% Magazin
    5291.6h  1.02% Programmende
    5068.8h  0.98% E-Sport
    4929.6h  0.95% Sitcom
    4785.4h  0.93% Wetterbericht
    4661.2h  0.90% Börsenmagazin
    4327.2h  0.84% Quiz
    4028.8h  0.78% Komödie
    3908.6h  0.76% Wissensmagazin
    3889.8h  0.75% Wirtschaftsmagazin
    3871.7h  0.75% Musikmagazin
    3703.6h  0.72% Telenovela
    3554.6h  0.69% Politikmagazin
    3442.2h  0.67% Realityshow
