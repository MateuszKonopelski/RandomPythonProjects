# Files

fdir = '/Users/panpluto/Documents/PROJECTS/Python_wprowadzenie/DATA/'

myfile = open(fdir + 'FMW00040308.dly')
print(myfile.readline())
print(myfile.readline()[0:17])
print('atribute: ', myfile.readline()[17:22])

myfile2 = open(fdir + 'Stations.txt', 'w')

# Read lines from file that indicate station name and date of observation
for line in open(fdir + 'FMW00040308.dly'):
    if line[17:21] == 'TAVG':
        writeline = str('station: ' + line[0:7] + ' Date: ' + line[7:13] + ' Time: ' + line[13:17] + '\n')
        myfile2.write(writeline)            # Save into new file

# Clear bufor
myfile.close()
myfile2.close()

print(type(myfile))         # test