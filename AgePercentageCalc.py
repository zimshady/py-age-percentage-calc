import csv
from Tkinter import *
from collections import *

# class popupWindow(object):
    # def __init__(self,master):
        # top=self.top=Toplevel(master)
        # self.l=Label(top,text="Hello World")
        # self.l.pack()
        # self.e=Entry(top)
        # self.e.pack()
        # self.b=Button(top,text='Ok',command=self.cleanup)
        # self.b.pack()
    # def cleanup(self):
        # self.value=self.e.get()
        # self.top.destroy()

class mainWindow:       
	def __init__(self, master):     
		self.filename=""
		
		def labels (Arch=0,Palaeop=0,Mesop=0,Neop=0,Palaeoz=0,Mesoz=0,Cenoz=0):
			lblArch=Label(root, text="Percentage Archaean Ages: "+str(Arch)+"%").grid(row=1, column=2)
			lblPalaeop=Label(root, text="Percentage Palaeoproterozoic Ages: "+str(Palaeop)+"%").grid(row=2, column=2)
			lblMesop=Label(root, text="Percentage Mesoproterozoic Ages: "+str(Mesop)+"%").grid(row=3, column=2)
			lblNeop=Label(root, text="Percentage Neoproterozoic Ages: "+str(Neop)+"%").grid(row=4, column=2)
			lblPalaeoz=Label(root, text="Percentage Palaeozoic Ages: "+str(Palaeoz)+"%").grid(row=5, column=2)
			lblMesoz=Label(root, text="Percentage Mesozoic Ages: "+str(Mesoz)+"%").grid(row=6, column=2)
			lblCenoz=Label(root, text="Percentage Cenozoic Ages: "+str(Cenoz)+"%").grid(row=7, column=2)

		labels()
		
		#Buttons  
		self.cbutton= Button(root, text="OK", command=lambda:self.process_csv(labels))
		self.cbutton.grid(row=10, column=3, sticky = W + E)
		self.bbutton= Button(root, text="Browse", command=self.browsecsv)
		self.bbutton.grid(row=1, column=3)
		self.abutton=Button(root, text="Save to CSV", command=lambda:self.writeCSV(self.process_csv,labels))
		self.abutton.grid(row=10,column=4)

	def browsecsv(self):
			from tkFileDialog import askopenfilename

			Tk().withdraw() 
			self.filename = askopenfilename()
	
	def process_csv(self,labelfunc):
		if self.filename:
			totalanalyses=0
			with open(self.filename) as csvfile:
				reader = csv.DictReader(csvfile)
				header = list(reader.fieldnames)
				displayfilename=Label(root, text=header[0]).grid(row=1,column=1)
				EndArchaean=float(2500)
				EndPalaeoprot=float(1600)
				EndMesoprot=float(1000)
				EndNeoprot=float(541)
				EndPalaeoz=float(252)
				EndMesoz=float(66)
				ArchaeanCount=0
				PalaeopCount=0
				MesopCount=0
				NeopCount=0
				PalaeozCount=0
				MesozCount=0
				CenozCount=0
				for row in reader:
					totalanalyses+=1
					if float(row[header[0]])>=EndArchaean:
						ArchaeanCount+=1
					elif float(row[header[0]])<=EndArchaean and float(row[header[0]])>=EndPalaeoprot:
						PalaeopCount+=1
					elif float(row[header[0]])<=EndPalaeoprot and float(row[header[0]])>=EndMesoprot:
						MesopCount+=1
					elif float(row[header[0]])<=EndMesoprot and float(row[header[0]])>=EndNeoprot:
						NeopCount+=1
					elif float(row[header[0]])<=EndNeoprot and float(row[header[0]])>=EndPalaeoz:
						PalaeozCount+=1
					elif float(row[header[0]])<=EndPalaeoz and float(row[header[0]])>=EndMesoz:
						MesozCount+=1
					else:
						CenozCount+=1

			def percent(part,whole):
				percentage=round((float(part)/float(whole)*100),2)
				return percentage
			
			Archpercent=0
			Palaeoppercent=0
			Mesoppercent=0
			Neoppercent=0
			Palaeozpercent=0
			Mesozpercent=0
			Cenozpercent=0
			Totalpercent=0
			Archpercent = percent(ArchaeanCount,totalanalyses)
			Palaeoppercent = percent(PalaeopCount,totalanalyses)
			Mesoppercent = percent(MesopCount,totalanalyses)
			Neoppercent = percent(NeopCount,totalanalyses)
			Palaeozpercent = percent(PalaeozCount,totalanalyses)
			Mesozpercent = percent(MesozCount,totalanalyses)
			Cenozpercent = percent(CenozCount,totalanalyses)
			
			dictpercent = OrderedDict([
					("Archaean",Archpercent),
					("Palaeoproterozoic",Palaeoppercent),
					("Mesoproterozoic",Mesoppercent),
					("Neoproterozoic",Neoppercent),
					("Palaeozoic",Palaeozpercent),
					("Mesozoic",Mesozpercent),
					("Cenozoic",Cenozpercent)
			])
			
			Totalpercent = Archpercent+Palaeoppercent+Mesoppercent+Neoppercent+Palaeozpercent+Mesozpercent+Cenozpercent
			
			if round(Totalpercent,0)!=100:
				print("Not 100 percent")
			else:
				labelfunc(Archpercent,Palaeoppercent,Mesoppercent,Neoppercent,Palaeozpercent,Mesozpercent,Cenozpercent)
				return dictpercent
				
	def writeCSV(self,fndata,labels2):
		data = fndata(labels2)
		print(data.items())
		print(type(data))
		if self.filename:
			with open('some.csv','wb') as csvfile:
				data = fndata(labels2)
				w = csv.DictWriter(csvfile, data.keys())
				w.writeheader()
				w.writerow(data)
	

root = Tk()
window=mainWindow(root)
root.mainloop()
