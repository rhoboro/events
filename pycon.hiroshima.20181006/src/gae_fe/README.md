# GAE FE

1. 下記のコマンドで作成

    ```sh
    $ gcloud config set project rhoboro-sandbox
    $ gcloud app deploy --version fe
    ```

# [GKEで動かす](https://cloud.google.com/appengine/docs/flexible/python/run-flex-app-on-kubernetes)

移行しやすくされているだけであおそらく最低限のデフォルト設定で動いています。
（k8sを使いこなすには設定ファイルで管理する必要があります。）

1. 下記のコマンドで作成

    ```sh
    $ gcloud config set project rhoboro-sandbox
    $ gcloud builds submit --tag gcr.io/rhoboro-sandbox/pyconhiro:latest .
    $ gcloud container clusters create mycluster
    $ gcloud config set compute/zone asia-northeast1-a
    $ gcloud container clusters get-credentials mycluster
    $ kubectl run mydeployment --image=gcr.io/rhoboro-sandbox/pyconhiro:latest --port:8080
    $ kubectl expose deployment mydeployment --type="LoadBalancer"
    $ kubectl get service mydeployment
    ```

1. クリーンアップ

    ```sh
    $ kubectl delete service --all
    $ gcloud container clusters delete
    ```
