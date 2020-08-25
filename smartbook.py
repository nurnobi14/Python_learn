import pyttsx3
import PyPDF2
my_book = open('c++.pdf', 'rb')
book_reader = PyPDF2.PdfFileReader(my_book)
total_pages = book_reader.numPages
print(total_pages)

engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('volume',0.5)
read_page = book_reader.getPage(3)
boo_text = read_page.extractText()
engine.say(boo_text)
#engine.say("you are check your pdf book pages number")
engine.runAndWait()