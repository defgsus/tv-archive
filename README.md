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

**109** channels, **1,190,962.2** hours playtime between **2023-01-17** and **2024-12-20**


### playtime per genre (top 30)

    77966.9h 6.55% Nachrichten
    54107.8h 4.54% Verkaufsshow
    49663.6h 4.17% Krimiserie
    43985.1h 3.69% Werbesendung
    37035.6h 3.11% Dokureihe
    35209.1h 2.96% Dokusoap
    34884.8h 2.93% Regionalmagazin
    31486.0h 2.64% Dokumentation
    28136.8h 2.36% *unknown*
    22333.3h 1.88% Zeichentrickserie
    22061.8h 1.85% Infomercial
    21303.2h 1.79% Animationsserie
    16883.0h 1.42% Comedyserie
    16709.6h 1.40% Morgenmagazin
    15797.8h 1.33% Talkshow
    15700.8h 1.32% Religionsmagazin
    14669.2h 1.23% Magazin
    11789.6h 0.99% E-Sport
    11460.4h 0.96% Sitcom
    10776.1h 0.90% Wetterbericht
    10564.4h 0.89% Quiz
    10519.7h 0.88% Komödie
    10496.2h 0.88% Programmende
    9201.2h  0.77% Realityshow
    9112.9h  0.77% Politikmagazin
    8914.2h  0.75% Wissensmagazin
    8713.2h  0.73% Börsenmagazin
    7956.1h  0.67% Wirtschaftsmagazin
    7917.3h  0.66% Dramaserie
    7909.5h  0.66% Telenovela
