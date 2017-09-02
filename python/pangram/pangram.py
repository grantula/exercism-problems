def is_pangram(string):
   letters = 'abcdefghijklmnopqrstuvwxyz'
   return all([x in string.lower() for x in letters])
