同一フォルダ内にあるjika.csvファイルを読み込み

1行目はヘッダー行として処理し

2行目以降に関しては

1,2,3,9列目のデータを取り出し

2列目のデータに関しては文字列になっているものを,

 $と,表記を削除し
 
 数値に変換し

9列のデータに関しては

 これも文字列になっているので
 
 半角スペースより左の文字を取り出し
 
 これを数値に変換し

変数 kijyunに2行9列名のデータの数値を代入し

数値に変換された各行9列目のデータ/kijyun*3列目の数値

 の値を10列目に設定し

同一フォルダー内に

jika_converted.csvと言うファイル名で出力し、保存する
