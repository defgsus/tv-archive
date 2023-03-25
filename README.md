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

**96** channels, **122,826.4** hours playtime between **2023-01-17** and **2023-03-26**


### playtime per genre (top 30)

    8605.4h 7.01% Nachrichten
    6168.6h 5.02% Verkaufsshow
    5121.4h 4.17% Krimiserie
    4149.8h 3.38% Werbesendung
    3851.9h 3.14% Dokusoap
    3788.9h 3.08% Dokureihe
    3608.7h 2.94% Regionalmagazin
    3049.6h 2.48% Dokumentation
    2843.5h 2.32% *unknown*
    2340.4h 1.91% Animationsserie
    2259.1h 1.84% Infomercial
    2232.7h 1.82% Zeichentrickserie
    2011.8h 1.64% Comedyserie
    1747.8h 1.42% Morgenmagazin
    1704.1h 1.39% Programmende
    1628.2h 1.33% Talkshow
    1587.5h 1.29% Religionsmagazin
    1273.0h 1.04% Magazin
    1269.2h 1.03% E-Sport
    1177.8h 0.96% Sitcom
    1135.5h 0.92% Börsenmagazin
    1098.0h 0.89% Wetterbericht
    1004.0h 0.82% Wirtschaftsmagazin
    960.5h  0.78% Wissensmagazin
    922.9h  0.75% Quiz
    920.3h  0.75% Musikmagazin
    894.3h  0.73% Dramaserie
    859.2h  0.70% Telenovela
    851.0h  0.69% Gesundheitsmagazin
    841.0h  0.68% Sportmagazin
