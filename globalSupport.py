import re, sys, os, shutil, operator
from collections import OrderedDict
	
def freq_patterns(inputFolder, outputFolder):

	for k in range(0,10):
	
		fileName = 'R'+str(k)
		
		f = open(inputFolder+"/"+fileName+".txt","r")
	
		#temporary lists for storing files and blocks
		filesList = []
		finalFilesList = []
		tempBlocksList = []
		finalBlocksList = []
		tempFileBlockList=[]
		tempFileBlockFinalList=[]
		tempFileBlockFinalList2=[]
		dataList = []
		finalDataList = []
		fileSupport={}
		blockSupport={}
		fileForPattern=[]
		tempDictBlockList=[]
		fileBlockDict={}
		forpattern=[]
		forpattern2=[]
		tempfeqele=[]
		tempfeqele2=[]
		pattern=""
		pattern2=""
		pattern3=""
		finalPattern=[]
		finalPattern2=[]
		finalPattern3=[]
		fileSupport2={}
		file=[]
		filesListPattern=[]
		a_temp=[]
		b_temp=[]
		a_temp2=""
		b_temp2=""
			
		print("Scanning Files for "+fileName)	
		print("Initiating the process "+fileName)
		#print("Caclulating File support, do not close the terminal\n")
		
		f2 = open(outputFolder+"/"+fileName.rstrip('.txt')+"-GlobalBlockSupport.txt","a+")
		
		print("Caclulating Block support, do not close the terminal "+fileName)
		
		#seggregating blocks files wise and storing in temporary files
		#..................................................................................................................................................
			
		f6=open(inputFolder+"/"+fileName+".txt","r")
		
		for x in f6:
			filesList.extend(re.findall('F[0-9]*[0-9]',x)) #files list
		
		for x in filesList:
			if not x in finalFilesList:
				finalFilesList.append(x) #Deleting duplicate files for getting the files list
				l=filesList.count(x) #Calculating file support
				fileSupport[x]=l #Stroring file support in a dictonary
				fileSupport2[fileName.rstrip(".txt")+" "+x]=l
		
		for y in finalFilesList:
			f4 = open(inputFolder+"/"+fileName+".txt","r")
			for x in f4:
				if re.search(y+" ",x):
					tempFileBlockList.extend(re.findall('B[0-9]*[0-9]',x))
					for k in tempFileBlockList:
						if not k in tempFileBlockFinalList:
							tempFileBlockFinalList.append(k)
							
					tempFileBlockFinalList2.extend(tempFileBlockFinalList)
				del tempFileBlockFinalList[:]
				del tempFileBlockList[:]
			
			f3 = open("temp_global/"+fileName.rstrip(".txt")+"_temp/"+fileName.rstrip(".txt")+" "+y+".txt","a+")
			for z in tempFileBlockFinalList2:
				f3.write(z + "\n")
			f3.close()
	
			del tempFileBlockFinalList[:]
			del tempFileBlockFinalList2[:]
			f4.close()
			
		#Calculating File-Block support			
		for x in finalFilesList:
			f5= open("temp_global/"+fileName.rstrip(".txt")+"_temp/"+fileName.rstrip(".txt")+" "+x+".txt","r")
			for y in f5:
				r=y.rstrip('\n')
				tempBlocksList.append(str(r))
		
			for z in tempBlocksList:
				if not z in finalBlocksList:
					finalBlocksList.append(z)
						
			for b in finalBlocksList:
				q=float(tempBlocksList.count(b))
				w=float(fileSupport[x])	
				support2=q/w
				support=round(support2,2)
				if support >= 0.6:
					blockSupport[fileName.rstrip('.txt')+" "+x+" "+b+" "]=str(support) 
					tempDictBlockList.extend(b)
					forpattern.append(fileName.rstrip('.txt')+" "+x)
					f9=open("temp_global/"+fileName.rstrip(".txt")+"_temp/FrequentPatterns/"+fileName.rstrip('.txt')+" "+x+".txt","a+")
					f9.writelines(b+"\n")
					f9.close()
			fileBlockDict[x]=tempDictBlockList	
			del tempBlocksList[:]
			del finalBlocksList[:]
			del tempDictBlockList[:]
		fileBlockDict.clear()
		fileSupport.clear()
		del filesList[:]
		del finalFilesList[:]
		
		blockSupportSorted = sorted(blockSupport, key=blockSupport.get, reverse=True)
			
		for x in blockSupportSorted:
			f2.writelines(x+" "+blockSupport[x]+"\n")
		
		del blockSupportSorted[:]
		blockSupport.clear()
	
	#................................................................................................................................
	
		
		for z in forpattern:
			if not z in forpattern2:
				forpattern2.append(z)	
			
		f8= open(outputFolder+"/"+fileName.rstrip('.txt')+"-GlobalFrequentPattern.txt","a+")
		
		###
		print("Creating Frequent Patterns "+fileName)
		for x in forpattern2:
			f10=open(inputFolder+"/"+fileName+".txt","r")
			a_temp.extend(re.findall('R[0-9]',x))
			b_temp.extend(re.findall('F[0-9]*[0-9]',x))
			
			a_temp2=a_temp[0]
			b_temp2=b_temp[0]
			
			for y in f10:
				if a_temp2+" " and b_temp2+" " in y:
					f11=open("temp_global/"+fileName.rstrip(".txt")+"_temp/FrequentPatterns/"+x+".txt","r")
					
					for z in f11:
						if z.rstrip('\n')+"" in y:
							tempfeqele.append(z)
					
					for p in tempfeqele:
						if not p in tempfeqele2:
							tempfeqele2.append(p)	
					
					del tempfeqele[:]	
					
					if len(tempfeqele2) > 0:
						for d in tempfeqele2:		
							pattern=pattern+d.rstrip('\n')+" "
					
						pattern2=x+" "+pattern
					
						finalPattern.append(pattern2)
					
						pattern=""
						pattern2=""
					f11.close()
					del a_temp[:]
					del b_temp[:]
					del tempfeqele2[:]
		
			del tempfeqele[:]
			del tempfeqele2[:]
			f10.close()
		
			
		for x in finalPattern:
			if not x in finalPattern2:
				finalPattern2.append(x)
				
		for x in finalPattern:	
			filesListPattern.extend(re.findall('F[0-9]*[0-9]',x))	
		
		for x in finalPattern2:
			file.append(re.findall('F[0-9]*[0-9]',x))
			a=float(finalPattern.count(x))
			b=float(filesListPattern.count(file[0][0]))
			sup=a/b
			sup2=round(sup,2)
			f8.writelines(x+" "+str(sup2)+"\n")
			del file[:]
		###
		
		#f.close(); f2.close(); f4.close(); f5.close()    (re.findall('R[0-9]+ D[0-9]*[0-9]+ F[0-9]*[0-9]',x))
		
		#removing all temporary files created	
		#shutil.rmtree('temp')
		
		print("Sucessfully done!!! \nCheck the output folder")