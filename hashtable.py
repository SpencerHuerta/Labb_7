from csv import reader
class HashNode:
   def __init__(self, key = "", data = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:
   def __init__(self, size):
      """size: hashtabellens storlek"""
      self.size = size
      #Fyll i kod här!
      self.slots = [None] * self.size

   def store(self, key, data):
      """key är nyckeln
         data är objektet som ska lagras
         Stoppar in "data" med nyckeln "key" i tabellen."""
      #Fyll i kod här!
      slot = self.hashfunction(key)
     # print(slot)
      if self.slots[slot] == None:
         self.slots[slot] = [HashNode(key,data)]
      else:
         i = 0
         for node in self.slots[slot]:
            if node.key == key:
               self.slots[slot][i].data = data
               return
            i+=1
         self.slots[slot].append(HashNode(key,data))


   def search(self, key):
      """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
      #Fyll i kod här!
      #...
      slot = self.hashfunction(key)
      if self.slots[slot] != None:
         for node in self.slots[slot]:
            if node.key == key:
               return node.data
         raise KeyError
      else:
         raise KeyError

   def hashfunction(self, key):
      """key är nyckeln
         Beräknar hashfunktionen för key"""
      #Fyll i kod här!
      # jag tänker att vi kan ta key som är namnet på dramat, 
      # separera orden och ta summan av bokstav för bokstav i ordet dvs. sum(ord(bokstav)) 
      # summera orden i namnet och ta remainder med antalet platser. 
      # frågan är hur mǻaga platser som ska ansättas. ska det vara lika med antalet rader i .csv 
      # eller ska vi lägga till några för att få en lite luftigare lista? 
      # jag tänker att jag testar att använda chaining till en början 
      i = 0
      for word in key.split():
         listword = list(word)
         for letter in listword:
            i += ord(letter)
     # return(i%(self.size))
      return 0





if __name__ == '__main__':
   def read_drama():
      with open('kdrama.csv', newline='') as csvfile:
         kdrama = reader(csvfile)
         rubriker = next(kdrama)
         draman = Hashtable(300)
         for rad in kdrama:
               draman.store(rad[0],rad)
               
      return draman

   draman = read_drama()
  