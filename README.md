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

**108** channels, **846,965.2** hours playtime between **2023-01-17** and **2024-05-11**


### playtime per genre (top 30)

    55299.2h 6.53% Nachrichten
    40433.4h 4.77% Verkaufsshow
    34491.8h 4.07% Krimiserie
    29619.7h 3.50% Werbesendung
    26690.2h 3.15% Dokureihe
    25592.8h 3.02% Dokusoap
    24655.0h 2.91% Regionalmagazin
    21940.6h 2.59% Dokumentation
    21587.5h 2.55% *unknown*
    15573.5h 1.84% Zeichentrickserie
    15401.0h 1.82% Infomercial
    15080.1h 1.78% Animationsserie
    12807.2h 1.51% Comedyserie
    11990.7h 1.42% Magazin
    11958.1h 1.41% Morgenmagazin
    11439.6h 1.35% Religionsmagazin
    11290.5h 1.33% Talkshow
    8404.1h  0.99% E-Sport
    7854.7h  0.93% Programmende
    7810.3h  0.92% Sitcom
    7525.6h  0.89% Wetterbericht
    7463.8h  0.88% Börsenmagazin
    7327.4h  0.87% Quiz
    7244.1h  0.86% Komödie
    6253.9h  0.74% Wissensmagazin
    6227.1h  0.74% Realityshow
    6226.8h  0.74% Politikmagazin
    6053.8h  0.71% Wirtschaftsmagazin
    6045.1h  0.71% Telenovela
    5627.1h  0.66% Musikmagazin
