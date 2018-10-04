1. 起動ディスクで`Container-Optimized OS ... stable` を選択する
1. Identity and API access は `Allow full access to all Cloud APIs` を選択する
  * スコープはフルオープンにしてIAMで管理するのがベストプラクティス
1. Firewallで`Allow HTTP traffic`にチェックをつける
1. 起動したら下記のコマンドを実行する

    ```sh
    $ docker-credential-gcr configure-docker
    $ docker run --rm -it -p 80:8080 asia.gcr.io/rhoboro-sandbox/appengine/default.fe
    ```
