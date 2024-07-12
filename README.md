# wCloud-WebApp
A web app based on the flask and [wCloud](https://github.com/sepinetam/wcloud)

# Navigate-language
- [ENGLISH](README.md)
- [中文](README.CN.md)

# Version
@Version0.0.1

# How to use
You could visit the [website](https://wcloud.tools.sepinetam.com) or you could clone this repo.

## Visit the website
Visit the [website](https://wcloud.tools.sepinetam.com) and use follow the next things:

- Upload your text-file with a extension in the list ```['txt', 'md']```
- Choose stopwords or upload your stopwords which is only ```'txt'``` allowed.
- Choose the other choice as you want
- Click the green button of ```生成词云✅```

## Use from your localhost
Clone the repo and run ```app.py```
```bash
git clone https://github.com/sepinetam/wcloud-webapp.git
cd wcloud-webapp

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py
```
And open your Browser(I prefer Chrome) and visit ```127.0.0.1:5000``` you will see the same page of the project [website](https://wcloud.tools.sepinetam.com).

# Acknowledgements
## Chinese fonts provider
Thanks to @[StellarCN](https://github.com/StellarCN) providing Chinese fonts from their [repo](https://github.com/StellarCN/scp_zh). Wishing StellarCN continued success.

## Make a demand
Thanks to Sociology and Political Science student @[Esme](mailto:esme2004dash@163.com) from Shanghai University for the demand, which inspired me to make this web app.
