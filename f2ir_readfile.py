# Read the file.
line: str = ""
width: int = int(self.text_stream.readLine())
temp: list[str] = self.text_stream.readLine()
for i in range(len(temp)):
    if i % width == 0:
        data.append(line)
        line = ""
    line += temp[i]
data.append(line)
return data