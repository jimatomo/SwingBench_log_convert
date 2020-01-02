# SoeLogFormat.py
# 2020/01/02 aythor:jimatomo
# python2 is not supported (python 3.6 or above is recommended)
import csv
import re
import sys
import argparse

# メインメソッド
def main(inputFilePath, outputFilePath):
    # inputFilePathは変換したいログファイルをフルパスで指定
    # outputFilePathは任意（入力しない場合はインプットファイル名の「.log」を「.csv」に変換）  
    if outputFilePath is None:
        outputFilePath = inputFilePath
        if outputFilePath[-4:] == '.log':
            outputFilePath = outputFilePath[:-4] + '.csv'
            
    try:
        # inputFilePathからファイルを文字列として読み込む
        with open(inputFilePath, newline='') as f:
            inputFile = f.read()

        # cleasingToList関数を使用してリストに変換
        metricList = cleasingToList(inputFile)

        # csvとして書き出す
        with open(outputFilePath, "w", encoding="Shift_jis") as f:
            # 文字コードをShift_JISに指定
            # writerオブジェクトの作成 改行記号で行を区切る
            writer = csv.writer(f, lineterminator="\n")
            writer.writerows(metricList)

        sys.exit()
        
    except (FileExistsError, FileNotFoundError) as e:
        print(e)
        sys.exit(1)


# テキストをListに変換してクレンジング
def cleasingToList(text):
    # inputしたログファイルから余分な空白を削除してcsv化
    formatedText = re.sub(r" +", " ", text).replace(' ', ',')
    
    # csv化したログファイルをList化する
    formatedList = []
    for row in csv.reader(formatedText.strip().splitlines()):
        formatedList.append(row)
    
    # 不要なSavedの列を削除（後ろから2番目に来ちゃう）
    if formatedList[len(formatedList)-2][0] == 'Saved':
        del formatedList[len(formatedList)-2]
    
    return formatedList


# コマンドライン引数を受け取る処理
parser = argparse.ArgumentParser(description='Swingbenchの冗長出力のログをクレンジングしてcsvに変換')
parser.add_argument('input', type=str, help='変換したいログファイルのフルパスを指定') 
parser.add_argument('-o', '--output', type=str, help='変換後のファイルのフルパスを指定可能')
args = parser.parse_args()


# メインメソッドに引数を渡す
if __name__ == '__main__':
    main(args.input, args.output)
