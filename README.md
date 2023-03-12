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

**96** channels, **101,121.8** hours playtime between **2023-01-17** and **2023-03-13**


### playtime per genre (top 30)

    7069.4h 6.99% Nachrichten
    5091.5h 5.04% Verkaufsshow
    4228.8h 4.18% Krimiserie
    3429.3h 3.39% Werbesendung
    3264.2h 3.23% Dokusoap
    3068.6h 3.03% Dokureihe
    2953.9h 2.92% Regionalmagazin
    2489.7h 2.46% Dokumentation
    2420.7h 2.39% *unknown*
    1936.6h 1.92% Animationsserie
    1853.0h 1.83% Infomercial
    1820.0h 1.80% Zeichentrickserie
    1625.0h 1.61% Comedyserie
    1418.0h 1.40% Morgenmagazin
    1390.2h 1.37% Programmende
    1339.1h 1.32% Talkshow
    1331.8h 1.32% Religionsmagazin
    1053.8h 1.04% E-Sport
    1040.0h 1.03% Magazin
    958.9h  0.95% Sitcom
    924.2h  0.91% Börsenmagazin
    892.6h  0.88% Wetterbericht
    818.4h  0.81% Wirtschaftsmagazin
    789.9h  0.78% Wissensmagazin
    748.7h  0.74% Musikmagazin
    745.9h  0.74% Quiz
    732.0h  0.72% Dramaserie
    701.1h  0.69% Gesundheitsmagazin
    695.3h  0.69% Telenovela
    652.2h  0.64% Sportmagazin
