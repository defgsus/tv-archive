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

**97** channels, **604,530.3** hours playtime between **2023-01-17** and **2023-12-20**


### playtime per genre (top 30)

    39688.4h 6.57% Nachrichten
    29028.0h 4.80% Verkaufsshow
    24420.3h 4.04% Krimiserie
    20549.8h 3.40% Werbesendung
    19657.7h 3.25% Dokureihe
    18162.3h 3.00% Dokusoap
    17496.5h 2.89% Regionalmagazin
    15500.9h 2.56% Dokumentation
    14822.4h 2.45% *unknown*
    11169.7h 1.85% Zeichentrickserie
    11014.0h 1.82% Infomercial
    10703.4h 1.77% Animationsserie
    9261.1h  1.53% Comedyserie
    8621.9h  1.43% Morgenmagazin
    8194.6h  1.36% Religionsmagazin
    8096.9h  1.34% Talkshow
    7800.8h  1.29% Magazin
    5962.6h  0.99% Programmende
    5948.1h  0.98% E-Sport
    5856.2h  0.97% Sitcom
    5528.7h  0.91% Wetterbericht
    5466.1h  0.90% Börsenmagazin
    5007.6h  0.83% Quiz
    4737.3h  0.78% Komödie
    4608.9h  0.76% Wissensmagazin
    4505.6h  0.75% Wirtschaftsmagazin
    4390.1h  0.73% Telenovela
    4369.9h  0.72% Musikmagazin
    4365.6h  0.72% Realityshow
    4296.7h  0.71% Politikmagazin
