class File:
   def __init__(self, filename, mode="r"):
       self.file = open(filename, mode)
       self.nrow = len(self.file.readlines())
       print("Number of rows:", self.nrow)
       self.file.seek(0)

   def __enter__(self):
       return self.file

   def __exit__(self, file_type, value, traceback):
       return self.file.close()


with File('log.txt') as file:
   for line in file:
       print(line.strip())
