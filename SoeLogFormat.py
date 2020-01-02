# SoeLogFormat.py
# 2020/01/02 aythor:jimatomo
# python 2.7 is supported
import csv
import re
import sys
import argparse
from io import open

def main(inputFilePath, outputFilePath): 
    if outputFilePath is None:
        outputFilePath = inputFilePath
        if outputFilePath[-4:] == '.log':
            outputFilePath = outputFilePath[:-4] + '.csv'
            
    try:
        # opening file from inputFilePath
        with open(inputFilePath, newline='') as f:
            inputFile = f.read()

        # cleasing to List via cleasingToList method
        metricList = cleasingToList(inputFile)
        
        # write to csv
        with open(outputFilePath, "wb") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerows(metricList)

        sys.exit()
        
    except Exception as e:
        print(e)
        sys.exit(1)


def cleasingToList(text):
    # format to csv (delete space and replace to canma)
    formatedText = re.sub(r" +", " ", text).replace(' ', ',')
    
    # convert to list
    formatedList = []
    for row in csv.reader(formatedText.strip().splitlines()):
        formatedList.append(row)
    
    # delete "Saved ..." line
    if formatedList[len(formatedList)-2][0] == 'Saved':
        del formatedList[len(formatedList)-2]
    
    return formatedList


# command line argment parsing
parser = argparse.ArgumentParser(description='cleasing and convert Swingbench verbose log file to csv')
parser.add_argument('input', type=str, help='path to input verbose log file') 
parser.add_argument('-o', '--output', type=str, help='path to output csv file')
args = parser.parse_args()


if __name__ == '__main__':
    main(args.input, args.output)
