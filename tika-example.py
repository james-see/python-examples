import tika
from tika import parser

parsed = parser.from_file("temp.wav")
print(parsed["metadata"])
print(parsed["content"])
exit()
