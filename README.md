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

**97** channels, **385,966.8** hours playtime between **2023-01-17** and **2023-08-19**


### playtime per genre (top 30)

    25572.9h 6.63% Nachrichten
    18218.1h 4.72% Verkaufsshow
    15613.4h 4.05% Krimiserie
    12995.8h 3.37% Werbesendung
    12769.6h 3.31% Dokureihe
    11694.5h 3.03% Dokusoap
    11094.5h 2.87% Regionalmagazin
    9738.5h  2.52% Dokumentation
    9384.9h  2.43% *unknown*
    7292.8h  1.89% Zeichentrickserie
    7048.2h  1.83% Infomercial
    6821.9h  1.77% Animationsserie
    6316.6h  1.64% Comedyserie
    5450.9h  1.41% Morgenmagazin
    5131.1h  1.33% Religionsmagazin
    5073.0h  1.31% Talkshow
    4783.2h  1.24% Magazin
    4281.6h  1.11% Programmende
    3827.7h  0.99% E-Sport
    3644.9h  0.94% Wetterbericht
    3622.1h  0.94% Sitcom
    3498.2h  0.91% Börsenmagazin
    3119.7h  0.81% Quiz
    3044.6h  0.79% Musikmagazin
    2974.4h  0.77% Komödie
    2957.8h  0.77% Wirtschaftsmagazin
    2893.8h  0.75% Wissensmagazin
    2702.6h  0.70% Telenovela
    2522.4h  0.65% Reportagereihe
    2483.5h  0.64% Sportmagazin
