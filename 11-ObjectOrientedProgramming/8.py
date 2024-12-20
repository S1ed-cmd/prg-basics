#Performer: Ed Sheeran
#Title:     Hearts Don't Break Around Here
#Album:     Divide
#Year:      2017

#Performer: Queen
#Title:     Bohemian Rhapsody
#Album:     A Night at the Opera
#Year:      1975
# class definition
class Song:
   def __init__(self,Performer,Title,Album,Year):
      self.Performer = Performer
      self.Title = Title
      self.Album = Album
      self.Year = Year
   def __str__(self):
          return (f"Performer: {self.artist}\n"
                f"Title:     {self.title}\n"
                f"Album:     {self.album}\n"
                f"Year:      {self.year}")

# object creation
song1 = ...
song2 = ...

## object usage
print(song1)
print(song2)
