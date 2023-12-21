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

**97** channels, **608,126.8** hours playtime between **2023-01-17** and **2023-12-22**


### playtime per genre (top 30)

    39948.0h 6.57% Nachrichten
    29203.2h 4.80% Verkaufsshow
    24565.5h 4.04% Krimiserie
    20673.3h 3.40% Werbesendung
    19771.0h 3.25% Dokureihe
    18261.5h 3.00% Dokusoap
    17630.3h 2.90% Regionalmagazin
    15605.1h 2.57% Dokumentation
    14916.1h 2.45% *unknown*
    11232.5h 1.85% Zeichentrickserie
    11078.9h 1.82% Infomercial
    10756.0h 1.77% Animationsserie
    9316.7h  1.53% Comedyserie
    8691.4h  1.43% Morgenmagazin
    8240.3h  1.36% Religionsmagazin
    8132.8h  1.34% Talkshow
    7866.3h  1.29% Magazin
    5990.7h  0.99% Programmende
    5987.6h  0.98% E-Sport
    5903.6h  0.97% Sitcom
    5561.0h  0.91% Wetterbericht
    5489.0h  0.90% Börsenmagazin
    5039.5h  0.83% Quiz
    4772.9h  0.78% Komödie
    4633.5h  0.76% Wissensmagazin
    4537.6h  0.75% Wirtschaftsmagazin
    4428.6h  0.73% Telenovela
    4406.1h  0.72% Realityshow
    4387.5h  0.72% Musikmagazin
    4328.1h  0.71% Politikmagazin
