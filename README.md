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

**97** channels, **591,959.8** hours playtime between **2023-01-17** and **2023-12-13**


### playtime per genre (top 30)

    38881.8h 6.57% Nachrichten
    28404.5h 4.80% Verkaufsshow
    23929.4h 4.04% Krimiserie
    20123.4h 3.40% Werbesendung
    19266.2h 3.25% Dokureihe
    17835.7h 3.01% Dokusoap
    17121.2h 2.89% Regionalmagazin
    15154.1h 2.56% Dokumentation
    14481.5h 2.45% *unknown*
    10936.6h 1.85% Zeichentrickserie
    10786.3h 1.82% Infomercial
    10502.7h 1.77% Animationsserie
    9114.6h  1.54% Comedyserie
    8437.7h  1.43% Morgenmagazin
    8023.3h  1.36% Religionsmagazin
    7931.9h  1.34% Talkshow
    7632.1h  1.29% Magazin
    5866.6h  0.99% Programmende
    5813.2h  0.98% E-Sport
    5726.4h  0.97% Sitcom
    5419.2h  0.92% Wetterbericht
    5377.4h  0.91% Börsenmagazin
    4913.3h  0.83% Quiz
    4606.3h  0.78% Komödie
    4510.2h  0.76% Wissensmagazin
    4423.9h  0.75% Wirtschaftsmagazin
    4295.9h  0.73% Musikmagazin
    4293.5h  0.73% Telenovela
    4241.6h  0.72% Realityshow
    4204.3h  0.71% Politikmagazin
