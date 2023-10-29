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

**97** channels, **514,737.2** hours playtime between **2023-01-17** and **2023-10-30**


### playtime per genre (top 30)

    33875.2h 6.58% Nachrichten
    24562.8h 4.77% Verkaufsshow
    20688.9h 4.02% Krimiserie
    17432.5h 3.39% Werbesendung
    16953.9h 3.29% Dokureihe
    15674.3h 3.05% Dokusoap
    14841.1h 2.88% Regionalmagazin
    13091.6h 2.54% Dokumentation
    12405.6h 2.41% *unknown*
    9600.9h  1.87% Zeichentrickserie
    9378.6h  1.82% Infomercial
    9202.6h  1.79% Animationsserie
    8141.1h  1.58% Comedyserie
    7284.9h  1.42% Morgenmagazin
    6934.8h  1.35% Religionsmagazin
    6856.5h  1.33% Talkshow
    6492.0h  1.26% Magazin
    5277.8h  1.03% Programmende
    5046.3h  0.98% E-Sport
    4903.7h  0.95% Sitcom
    4769.6h  0.93% Wetterbericht
    4647.9h  0.90% Börsenmagazin
    4303.3h  0.84% Quiz
    4030.8h  0.78% Komödie
    3893.9h  0.76% Wissensmagazin
    3875.0h  0.75% Wirtschaftsmagazin
    3864.1h  0.75% Musikmagazin
    3685.1h  0.72% Telenovela
    3533.9h  0.69% Politikmagazin
    3418.4h  0.66% Realityshow
