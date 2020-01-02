# SwingBench_log_convert
Swingbenchのログをcsvに変換するpythonスクリプト。 (Linux) 
convertするファイルの出力方法は後述を参照  
Converting a swingbench verbose output logfile to csvfile.

## ファイルの説明 (Script file description)
それぞれで実行可能なpythonのバージョンが異なります。
- SoeLogFormat.py : python2.7 is supported (and provide English help)
- SoeLogFormat_py3.py : python3.6 or later is supported (only Japanese help)

## 使用方法 (How to use) 
以下のように使用します。  
※`<logfile_path>`は変換するファイルのフルパスを指定します (eg. /ver/tmp/result.log)
```
python SoeLogFormat.py <logfile_path>
```

変換したcsvファイルは拡張子がcsvに変換され、同じパスに出力されます。（上書きされるので注意）  
出力先を指定する場合は以下のように出力先を指定可能
```
python SoeLogFormat.py <logfile_path> -o <convert_file_path>
```

## Swingbenchのログの出力方法
以下のように出力する。設定ファイルは任意のものを使用
```
cd <swingbench_home>/bin

./charbench \
  -c ../<config_file> \
  -r /var/tmp/swingbench_result_`date +%Y%m%d_%H%M%S`.xml \
  -stats full \
  -v tpm,tps,resp,vresp \
  -vo /var/tmp/swingbench_output_`date +%Y%m%d_%H%M%S`.log \
  -mr | tee /var/tmp/swingbench_stdout_`date +%Y%m%d_%H%M%S`.log
```
上記の`/var/tmp/swingbench_output_`date +%Y%m%d_%H%M%S`.log`をスクリプトの`<logfile_path>`に指定する。
