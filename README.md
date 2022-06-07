# AWS Lambda S3 CSVからRDS登録サンプル
## setup
- `cd src`
- 依存ライブラリのインストール
  - `pip install pymysql -t .`
- deploy用にzip作成
  - `zip ./deploy.zip ./*`
- 作成したzipをlambdaにアップロード

## 補足(インフラ周り)
- RDSをVPCに入れている場合
  - lambdaも同じVPC(セキュリティグループも)に入れる
  - セキュリティグループのインバウンド、アウトバウンドルールにカスタムTCP port:3306を許容するルール設定
  - 合わせてS3用のエンドポイントをセキュリティグループに設定
