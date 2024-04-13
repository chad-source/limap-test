## 目前修改部分
* Line mapping 和 Visualization 合在```test.py```裡，想說之後就直接跑```test.py```。
* 有建一個 npyfolder 可以把緩存檔存在那。
* 在```line_triangulation.py```裡的 A 部分有做一點修改：
  * 原本是想說 neighbor 直接幫他找好就不用跑```compute_sfminfos()```
  * 不過他有生一個 sfminfos_colmap_folder 後面會用到
  * 不確定裡面是甚麼也不確定能不能不跑```compute_sfminfos()```做出來
目前大概做這樣而已。
---
## 原本想法
* 圖片進來之後就存在一個資料夾
* 利用緩存檔把已經處理過的東西紀錄
* 只處理新進的圖片跟一些和新進圖片有關連的舊圖  
不過因為有蠻多變數的型別不確定，所以不太敢大改。
如果學長有想法的話，我也可以幫忙學長改。
