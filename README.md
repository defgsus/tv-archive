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

**97** channels, **432,401.9** hours playtime between **2023-01-17** and **2023-09-14**


### playtime per genre (top 30)

    28549.9h 6.60% Nachrichten
    20529.5h 4.75% Verkaufsshow
    17515.5h 4.05% Krimiserie
    14585.5h 3.37% Werbesendung
    14261.6h 3.30% Dokureihe
    13140.8h 3.04% Dokusoap
    12462.8h 2.88% Regionalmagazin
    10903.1h 2.52% Dokumentation
    10269.7h 2.38% *unknown*
    8165.2h  1.89% Zeichentrickserie
    7890.4h  1.82% Infomercial
    7661.4h  1.77% Animationsserie
    7019.9h  1.62% Comedyserie
    6118.0h  1.41% Morgenmagazin
    5781.2h  1.34% Religionsmagazin
    5727.5h  1.32% Talkshow
    5404.0h  1.25% Magazin
    4647.1h  1.07% Programmende
    4277.2h  0.99% E-Sport
    4083.7h  0.94% Wetterbericht
    4071.1h  0.94% Sitcom
    3927.8h  0.91% Börsenmagazin
    3570.8h  0.83% Quiz
    3401.8h  0.79% Musikmagazin
    3344.6h  0.77% Komödie
    3280.2h  0.76% Wirtschaftsmagazin
    3236.0h  0.75% Wissensmagazin
    3054.3h  0.71% Telenovela
    2851.3h  0.66% Reportagereihe
    2826.8h  0.65% Politikmagazin
