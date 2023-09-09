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

**97** channels, **425,284.3** hours playtime between **2023-01-17** and **2023-09-10**


### playtime per genre (top 30)

    28071.4h 6.60% Nachrichten
    20161.6h 4.74% Verkaufsshow
    17261.2h 4.06% Krimiserie
    14357.8h 3.38% Werbesendung
    14013.6h 3.30% Dokureihe
    12924.8h 3.04% Dokusoap
    12238.1h 2.88% Regionalmagazin
    10720.7h 2.52% Dokumentation
    10141.1h 2.38% *unknown*
    8030.7h  1.89% Zeichentrickserie
    7764.5h  1.83% Infomercial
    7530.1h  1.77% Animationsserie
    6903.3h  1.62% Comedyserie
    6006.8h  1.41% Morgenmagazin
    5684.7h  1.34% Religionsmagazin
    5606.1h  1.32% Talkshow
    5316.4h  1.25% Magazin
    4586.6h  1.08% Programmende
    4201.2h  0.99% E-Sport
    4021.0h  0.95% Wetterbericht
    3990.9h  0.94% Sitcom
    3844.5h  0.90% Börsenmagazin
    3501.4h  0.82% Quiz
    3358.1h  0.79% Musikmagazin
    3315.2h  0.78% Komödie
    3224.5h  0.76% Wirtschaftsmagazin
    3176.1h  0.75% Wissensmagazin
    2995.6h  0.70% Telenovela
    2797.8h  0.66% Reportagereihe
    2760.0h  0.65% Politikmagazin
