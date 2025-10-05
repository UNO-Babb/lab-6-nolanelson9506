#WordCount.py
#Name:Nola Nelson
#Date:10/05/25
#Assignment:Lab6

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount +1
      for ch in w:
        letterCount = letterCount + 1
    
  
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)


if __name__ == '__main__':
  main()
