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

**109** channels, **1,173,596.0** hours playtime between **2023-01-17** and **2024-12-09**


### playtime per genre (top 30)

    76675.4h 6.53% Nachrichten
    53414.0h 4.55% Verkaufsshow
    48937.2h 4.17% Krimiserie
    43277.7h 3.69% Werbesendung
    36588.4h 3.12% Dokureihe
    34813.9h 2.97% Dokusoap
    34339.2h 2.93% Regionalmagazin
    30931.9h 2.64% Dokumentation
    27688.0h 2.36% *unknown*
    22006.2h 1.88% Zeichentrickserie
    21715.3h 1.85% Infomercial
    20981.0h 1.79% Animationsserie
    16698.2h 1.42% Comedyserie
    16425.5h 1.40% Morgenmagazin
    15578.6h 1.33% Talkshow
    15565.3h 1.33% Religionsmagazin
    14536.6h 1.24% Magazin
    11591.6h 0.99% E-Sport
    11307.0h 0.96% Sitcom
    10603.3h 0.90% Wetterbericht
    10365.1h 0.88% Quiz
    10350.2h 0.88% Programmende
    10349.4h 0.88% Komödie
    9044.5h  0.77% Realityshow
    8933.2h  0.76% Politikmagazin
    8802.6h  0.75% Wissensmagazin
    8647.0h  0.74% Börsenmagazin
    7838.0h  0.67% Wirtschaftsmagazin
    7768.4h  0.66% Telenovela
    7763.2h  0.66% Dramaserie
