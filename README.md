## 開発方法

### Docker を使う場合

```shell
docker compose build
docker compose up
```

### Docker を使わない場合

```shell
pip install -r ./requirements.txt

# 必要に応じてフォーマッタをインストール

uvicorn main:app --reload

# Debug: python main.py
```

各フォーマッタの実行ファイルは，以下に書いている方法でインストールできます．
#### clang-format (C/C++)
brew/apt などでインストールしてください．
```shell
apt update && apt install -y clang-format

brew install clang-format
```

#### black (Python)
```shell
pip install black
```

#### dotnet-format (C#)
```shell
dotnet tool install -g dotnet-format
```
