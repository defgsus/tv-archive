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

**96** channels, **332,113.0** hours playtime between **2023-01-17** and **2023-07-20**


### playtime per genre (top 30)

    22105.1h 6.66% Nachrichten
    15876.3h 4.78% Verkaufsshow
    13336.2h 4.02% Krimiserie
    11144.4h 3.36% Werbesendung
    10845.3h 3.27% Dokureihe
    10037.6h 3.02% Dokusoap
    9524.4h  2.87% Regionalmagazin
    8359.6h  2.52% Dokumentation
    8114.6h  2.44% *unknown*
    6321.9h  1.90% Zeichentrickserie
    6068.9h  1.83% Infomercial
    5854.1h  1.76% Animationsserie
    5494.5h  1.65% Comedyserie
    4659.8h  1.40% Morgenmagazin
    4402.6h  1.33% Talkshow
    4401.9h  1.33% Religionsmagazin
    3944.8h  1.19% Magazin
    3872.5h  1.17% Programmende
    3295.1h  0.99% E-Sport
    3153.6h  0.95% Sitcom
    3103.1h  0.93% Wetterbericht
    2990.7h  0.90% Börsenmagazin
    2650.5h  0.80% Quiz
    2602.1h  0.78% Musikmagazin
    2570.5h  0.77% Wirtschaftsmagazin
    2537.0h  0.76% Wissensmagazin
    2521.2h  0.76% Komödie
    2309.2h  0.70% Telenovela
    2200.9h  0.66% Sportmagazin
    2116.4h  0.64% Dramaserie
