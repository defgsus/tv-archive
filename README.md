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

**110** channels, **1,277,634.9** hours playtime between **2023-01-17** and **2025-02-17**


### playtime per genre (top 30)

    83833.4h 6.56% Nachrichten
    57264.8h 4.48% Verkaufsshow
    53071.7h 4.15% Krimiserie
    47743.5h 3.74% Werbesendung
    39643.4h 3.10% Dokureihe
    37475.3h 2.93% Dokusoap
    37141.3h 2.91% Regionalmagazin
    34299.2h 2.68% Dokumentation
    30365.1h 2.38% *unknown*
    24123.8h 1.89% Zeichentrickserie
    23866.3h 1.87% Infomercial
    22879.9h 1.79% Animationsserie
    17845.4h 1.40% Morgenmagazin
    17775.0h 1.39% Comedyserie
    16894.7h 1.32% Talkshow
    16513.2h 1.29% Religionsmagazin
    15184.4h 1.19% Magazin
    12676.6h 0.99% E-Sport
    12225.1h 0.96% Sitcom
    11660.8h 0.91% Komödie
    11598.0h 0.91% Wetterbericht
    11383.9h 0.89% Quiz
    11177.4h 0.87% Programmende
    9953.0h  0.78% Realityshow
    9779.1h  0.77% Politikmagazin
    9359.6h  0.73% Wissensmagazin
    8946.0h  0.70% Börsenmagazin
    8506.1h  0.67% Arztserie
    8501.6h  0.67% Dramaserie
    8436.6h  0.66% Wirtschaftsmagazin
