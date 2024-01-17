data: list[str] = []
# Read the file.
width: int = int(self.text_stream.readLine())
height: int = int(self.text_stream.readLine())
for i in range(height):
    line: str = ""
    for j in range(width):
        line += self.text_stream.readLine()
    data.append(line)
return data