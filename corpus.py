with open("french-test.arff", "w", encoding="utf-8") as f:
  f.write(
    "@RELATION french\n\n"
    "@ATTRIBUTE text   string\n"
    "@ATTRIBUTE class  {FR,BE,LU,CA}\n\n"
    "@DATA\n"
  )
for TLD in ["FR", "BE", "LU", "CA"]:
  with open("FR-" + TLD + ".txt", "r", encoding="utf-8") as f:
    para = f.readlines()
  with open("french-test.arff", "a", encoding="utf-8") as f:
    for line in para:
      line = line.replace("\n", " ").replace("\"", "\\\"").replace("<doc", "\"<doc").replace("</doc>", "</doc>\", " + TLD + "\n")
      if line.count(' ') > 1:
        f.write(line)